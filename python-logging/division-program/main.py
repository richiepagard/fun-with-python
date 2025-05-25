import logging

logger = logging.getLogger(__name__)
# Set custom level for logger
logger.setLevel(logging.DEBUG)

# Declare handlers
file_handler = logging.FileHandler("logs/division_logs.log")
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
