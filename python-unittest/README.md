# Python Test (Unittest / Pytest)
A collection of exercises to practice and explore Python's built-in **`unittest`** module and the third-party **`pytest`** framework.

---

## Testing A Calculation Class

**Exercise Goal:** Create a `Calculator` class with `add`, `subtract`, `multiply`, and `divide` methods. Log all operations accurately.

### Test Coverage
- Test each method with various input types.
- Test edge cases like division by zero.
- Verify raised exceptions (e.g., `ZeroDivisionError`).
- Ensure logging is correctly handled.

---

## Mocking With Unittest -> Testing A URL Status Checker

**Exercise Goal:** Implement a function that sends an HTTP request to a given URL and returns the status code. Log relevant events and errors.

### Test Coverage Using Mock
- Use `unittest.mock` to simulate HTTP responses for different URLs and status codes (e.g., `200`, `404`, `timeout`).
- Verify logging of events and exceptions.

---

## File Processor -> Testing A File Processor Program

**Exercise Goal:** Write a program that reads a text file and returns the number of lines, words, and characters. A funny version of `wc` command in **UNIX**. Log all operations accurately.

### Test Coverage
- Test various situation a file might has!
- Test `unicode` maybe.
- Test edge cases and verify raised exceptions like `FileNotFoundError`.
- Ensure logging is correctly handled.
