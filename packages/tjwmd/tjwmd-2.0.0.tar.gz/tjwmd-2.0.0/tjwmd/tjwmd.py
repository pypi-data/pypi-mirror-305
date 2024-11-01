import math
from pathlib import Path
from typing import List, Union, Dict, Optional

import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

from .digits_labels import DigitsLabels
from .utils import resize_image, rotate_image, remove_invalid_counters, calculate_bbox_center, is_center_inside_box, \
    get_midpoint, angle_with_center


class TJWMD:
    def __init__(
            self,
            wm_counter_model_path: Union[str, Path],
            wm_digits_model_path: Union[str, Path],
            digits_labels: DigitsLabels = DigitsLabels(),
            counter_labels: Optional[List[str]] = None,
    ):
        self._wm_counter_model_path = wm_counter_model_path
        self._wm_digits_model_path = wm_digits_model_path
        self._digits_labels = digits_labels
        self._counter_labels = (
            counter_labels if counter_labels is not None
            else YOLO(wm_counter_model_path).names.values()
        )

    def _detect_counters(
            self,
            _image: Image,
            conf: float = 0.1
    ):
        model = YOLO(self._wm_counter_model_path)
        results = model.predict(
            source=_image,
            conf=conf
        )

        bboxes = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                c = box.cls
                if model.names[int(c)] in self._counter_labels:
                    bboxes.append(box.xyxy[0])

        return bboxes

    def _detect_digits(
            self,
            frame_,
            conf: float = 0.1,
    ):
        model = YOLO(self._wm_digits_model_path)
        results = model.predict(
            source=frame_,
            conf=conf
        )

        digits = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                c = box.cls
                digits.append((box.xyxy[0], model.names[int(c)]))

        return digits

    def _predict_values(
            self,
            _image: Image,
            num_of_digits: int,
            counters: list,
            conf: float = 0.1
    ):
        image = _image.copy()
        values = []
        for counter in counters:
            # bbox with label
            digits = self._detect_digits(image, conf)
            digits = list(sorted(digits, key=lambda x: x[0][0]))

            prev_digit = None
            valid_digits = []

            for digit in digits:
                bbox, label = digit
                actual_label = label

                is_valid_digits = False
                for i in range(10):
                    if label in self._digits_labels[i]:
                        actual_label = str(i)
                        is_valid_digits = True
                        break
                if not is_valid_digits:
                    continue

                center = calculate_bbox_center(bbox)

                if not is_center_inside_box(center, counter):
                    continue

                if prev_digit is None:
                    prev_digit = digit
                    valid_digits.append((digit, actual_label))
                    continue

                if is_center_inside_box(center, prev_digit[0]):
                    continue

                prev_digit_center = calculate_bbox_center(prev_digit[0])
                midpoint = get_midpoint(prev_digit_center, center)
                check_point = center if center[1] > prev_digit_center[1] else prev_digit_center
                angle = angle_with_center(check_point, midpoint)
                if 45 <= angle <= 135:
                    continue

                prev_digit = digit
                valid_digits.append((digit, actual_label))

            if len(valid_digits) == num_of_digits:
                annotator = Annotator(image)
                annotator.box_label(counter)
                for digit, label in valid_digits:
                    annotator.box_label(digit[0], label)
                values.append("".join([label for _, label in valid_digits]))

        return values, image

    def predict(
            self,
            _image: Image,
            num_of_digits: int,
            wm_counter_conf: float = 0.1,
            wm_digits_conf: float = 0.1,
            angle: float = None,
    ):
        # image preprocessing
        image = _image.copy()
        image = resize_image(image, (640, 640))
        if angle is not None:
            image = rotate_image(image, angle)

        # counters processing
        counters = self._detect_counters(image, wm_counter_conf)
        counters = remove_invalid_counters(counters)
        if not counters:
            return []

        return self._predict_values(
            image, num_of_digits,
            counters, wm_digits_conf
        )
