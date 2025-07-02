"""
Test cases for the file_processor function in the file_manager module.

Classes:
    TestFileProcessor: Contains tests for the file_processor function.
"""

import unittest
import tempfile

from file_manager.file_processor import file_processor


class TestFileProcessor(unittest.TestCase):
    """
    Test class for test different scenarios of the file_processor function.
    All methods create a temporary file with specific content or maybe no content at all.

    Methods:
        test_file_with_simple_content(self): Tests the file_processor function with a simple file content.
    """
    def test_file_with_simple_content(self):
        # Create a temporary file with simple content
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("Hello World\nThis is a simple content for a test file to test the file processor program.")
            temp_file.seek(0)

            line_count, word_count, char_count = file_processor(temp_file.name)

            self.assertEqual(line_count, 1)
            self.assertEqual(word_count, 17)
            # Only ascii letters counted
            self.assertEqual(char_count, 71)


if __name__ == '__main__':
    unittest.main()
