# Notes For Python Logging Module
I write some important or cool things I found in `logging` in this file to have my own notebook. Just for record what I could understand and what I found cool or important.

---

## Logger
Each logger is a specific **logger** (I could memorize it like this :/ ) can use in different part of a program with different configs.
Create a logger like this: `logger = logging.getLogger(__name__)`

## Handler
Determine where a specific log should go. We use handlers depends on our porpuse, for instance, I can use `SMTPHandler` to send me an email contains logs. In conclusion, handlers determine the behavior of logs when they create.

An example of a handler I've just wrote it in `division-program/main.py`:
```python
# Create handlers
file_handler = logging.FileHandler("logs/funny_life_logs.log")
stream_handler = logging.StreamHandler()

# Determine and set specific formatter for file handler
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
# Determine and set specific formatter for stream handler
stream_formatter = logging.Formatter("%(levelname)s - %(name)s - %(message)s")
stream_handler.setFormatter(stream_formatter)

# Set specific level for each handler
file_handler.setLevel(logging.WARNING)
stream_handler.setLevel(logging.DEBUG)

# Check if the logger does not have any handlers, then add the handlers to the logger
if not logger.hasHandlers:
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
```

- I created two handlers, one for files (`file_handler`) and another for stream which is shows in console (`stream_handler`).
- In the next step I set specific format for each handler.
- Then, I set specific level for each handler:
1. `WARNING` for file handler which means only warning level and more important levels will save or log to the file.
2. `DEBUG` for stream handler which means logs in debug and greater than that will show on the console.

- Last step is add handlers to the logger, for this first I checked logger doesn't have any handlers and then add handlers to it. This check is for duplicate handlers and prevent re-adding on imports.

---
