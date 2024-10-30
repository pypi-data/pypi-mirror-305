# My Logging Library

A custom logging library built on Python's standard logging module.

## Installation
pip install alex-tech-logging-library

## Usage

```python
from alex_tech_logging_library import setup_logger

logger = setup_logger('my_logger', 'app.log')

# Example log messages
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
```