# rennips

A minimalist Python progress **spinner** that provides a simple visual feedback for iterative processes with normal and simple display modes.

\> "*rennips*" is simply 'spinner' spelled backwards. 

Check out on [**PyPI**](https://pypi.org/project/rennips/0.1.0/)



## Installation

```bash
pip install rennips
```



## Usage

```python
import time
from rennips import rennips


data = [x for x in range(50)]
for i in rennips(data, desc="Counting...", mode="SIMPLE"):
    time.sleep(0.05)
```



## Features

- Simple spinner animation (**|, /, -, \\**)
- Progress percentage
- Item count
- Elapsed time
- Works with any iterable
- Support for iterables without known length



## Roadmap

Future features and improvements planned for Rennips:

### Short-term Goals
- [ ] Big mode: Large-scale spinner display for better visibility in terminal
- [ ] Manual spinner control: Support for non-iterable progress tracking, allowing start/stop/update operations
