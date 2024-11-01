# tjwmd

![PyPI - Version](https://img.shields.io/pypi/v/tjwmd)

## Installation

```shell
pip install tjwmd
```

## Quick Start

```python
from PIL import Image

from tjwmd import TJWMD
from tjwmd.digits_labels import DigitsLabels

dl = DigitsLabels()
dl[0] = ['0', 'Zero']

wmd = TJWMD(
    wm_counter_model_path='yolov8_wmc_v1.pt',
    wm_digits_model_path='yolov8_wmd_v3s.pt',
    digits_labels=dl,
    counter_labels=['counter']
)

img = Image.open('6724502e2cec9d702006b6cc.jpeg')

values, bbox_img = wmd.predict(
    _image=img,
    num_of_digits=6,
    wm_digits_conf=0.1,
    wm_counter_conf=0.1,
    angle=0.0
)
print(values)

bbox_img.show()
```