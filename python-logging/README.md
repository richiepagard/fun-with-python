# Python Logging Exercises
A collection of simple exercises to practice and explore Python's `logging` module.

---

## Log User Input

### Basic Logging
- **Ask for the user for their name.**
- **Log messages when:**
1. The script starts.
2. It receives inputs.
3. The script finishes.

---

### Log To File
- Modify the previous exercise to log messages to a file name instead of printing to the console.

---

### Customize Logging Format
- **Customize the log format to include:**
1. Timestamp
2. Log level
3. Message

This patterns: `%(asctime)s - %(levelname)s - %(message)s`

---

## Log Division Program

### Basic Logging
- **Ask user two number to divide them.**
- **Log messages when:**
1. The script starts.
2. It receives inputs.
3. The script finishes.
4. An exception occurs (like division by zero).

---

### Custom Logger Per Module
- **The project should have two files: `main.py` and `utils.py`.**
- **Each file uses its own logger (with `__name__`).**
- **`main.py` logs calls to functions from `utils.py`**

---

### Rotation logs
- **Use rotation logs to:**
1. Limit the log file size (e.g., 1 KB).
2. Automatically rotate the log when the size limit hit.

---
