import math
from typing import Tuple

from PIL import Image
from PIL.Image import Resampling


def resize_image(_image: Image, max_size: Tuple[int, int] = (800, 400)):
    image = _image.copy()
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image


def rotate_image(_image: Image.Image, angle: float) -> Image.Image:
    image = _image.copy()
    angle_rad = math.radians(-angle)
    cos = abs(math.cos(angle_rad))
    sin = abs(math.sin(angle_rad))

    w, h = image.size

    new_w = int(h * sin + w * cos)
    new_h = int(h * cos + w * sin)

    rotated_image = image.rotate(angle, resample=Resampling.BICUBIC, expand=True)

    result = Image.new("RGBA", (new_w, new_h))
    result.paste(rotated_image, ((new_w - rotated_image.width) // 2, (new_h - rotated_image.height) // 2))

    return result


def get_bbox_h_w(bbox):
    return bbox[3] - bbox[1], bbox[2] - bbox[0]


def calculate_bbox_center(bbox):
    return (
        (bbox[0] + bbox[2]) / 2,
        (bbox[1] + bbox[3]) / 2
    )


def is_center_inside_box(center, bbox):
    x_center, y_center = center
    x_min, y_min, x_max, y_max = bbox
    return x_min <= x_center <= x_max and y_min <= y_center <= y_max


def remove_invalid_counters(counters):
    if len(counters) == 0:
        return counters

    valid_counters = []
    prev_counter = None
    for counter in counters:
        h, w = get_bbox_h_w(counter)
        if h > w:
            continue

        if prev_counter is None:
            prev_counter = counter
            valid_counters.append(prev_counter)
            continue

        center = calculate_bbox_center(counter)
        if is_center_inside_box(center, prev_counter):
            continue

        valid_counters.append(prev_counter)
        prev_counter = counter

    return valid_counters


def get_midpoint(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return midpoint


def angle_with_center(point, center):
    x, y = point
    cx, cy = center
    angle_radian = math.atan2(y - cy, x - cx)
    angle_degree = math.degrees(angle_radian)
    if angle_degree < 0:
        angle_degree += 360
    return angle_degree
