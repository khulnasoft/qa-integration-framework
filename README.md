# qa-integration-framework
Khulnasoft QA framework for integration tests

## Installation

1. Clone the framework's repo: `git clone https://github.com/khulnasoft/qa-integration-framework.git`
2. Install python deps: `apt-get install python3 python3-dev python3-pip -y`
3. Install the framework: `pip install qa-integration-framework/`
    > It will also install all the dependencies from the requirements.txt automatically.

## Usage

You can just import it from the test suite as any other python library
```python
from khulnasoft_testing.constants.paths.logs import KHULNASOFT_LOG_PATH
from khulnasoft_testing.modules.analysisd import patterns
from khulnasoft_testing.tools.monitors.file_monitor import FileMonitor
from khulnasoft_testing.utils import callbacks


monitor = FileMonitor(KHULNASOFT_LOG_PATH)
monitor.start(callback=callbacks.generate_callback(patterns.ANALYSISD_STARTED))

```
