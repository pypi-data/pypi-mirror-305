# linux-capabilities

`linux-capabilities` is a Python library that provides an enumeration of Linux capabilities based on the [capabilities(7) Linux man page](https://man7.org/linux/man-pages/man7/capabilities.7.html).

## Installation

For a standard installation, use:
```
python3 -m pip install [--break-system-packages] py-linux-capabilities
```

To install from TestPyPI, use:

```
pip install -i https://test.pypi.org/simple/ py-linux-capabilities
```

## Build
```
python3 -m build
```

## Usage
```
from linux_capabilities import LinuxCapabilities

mycap = LinuxCapabilities.CAP_SYS_ADMIN
print(mycap)
```
