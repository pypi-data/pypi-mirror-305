from typing import List


class DigitsLabels:
    def __init__(self):
        self._labels = {i: [str(i)] for i in range(10)}

    def __setitem__(self, digit: int, labels: List[str]):
        if 0 <= digit <= 9:
            self._labels[digit] = labels
        else:
            raise ValueError("Digit must be between 0 and 9.")

    def __getitem__(self, digit: int) -> List[str]:
        if 0 <= digit <= 9:
            return self._labels[digit]
        else:
            raise ValueError("Digit must be between 0 and 9.")
