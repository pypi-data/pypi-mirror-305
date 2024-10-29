# My Logging Library

A custom logging library built on Python's standard logging module.

## Installation
pip install alex-tech-logging-library

## Usage

```python
from my_logging_library import get_logger

logger = get_logger('my_app', log_file='app.log')
logger.info('This is an info message')
logger.error('This is an error message')
```