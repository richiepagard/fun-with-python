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
        setUp (self): Method for prepare the test fixture.
        test_file_with_simple_content(self): Tests the file_processor function with a simple file content.
        test_file_with_no_content(self): Tests the function with an empty file.
        test_all_digits(self): Tests the function with all digit file content, tested `Richie` in binary for this.
        test_file_with_no_space(self): Tests the function with no space, tab, and newline content.
        test_file_with_only_newline(self): Tests the function with only a newline content.
        test_file_with_only_tab(self): Tests the function with only a tab content.
        test_file_with_only_space(self): Tests the function with only a white space content.
    """
    def setUp(self):
        """
        Prepares the test fixtures.
        Define 'line_count', 'word_count', and 'char_count' variables.
        """
        self.line_count = self.word_count = self.char_count = 0

    def test_file_with_simple_content(self):
        # Create a temporary file with simple content
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("Hello World\nThis is a simple content for a test file to test the file processor program.")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 1)
            self.assertEqual(self.word_count, 17)
            # Only ascii letters counted
            self.assertEqual(self.char_count, 71)

    def test_file_with_no_content(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 0)
            self.assertEqual(self.word_count, 0)
            self.assertEqual(self.char_count, 0)

    def test_all_digits(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("0101001\n001101001011000110110100\n00110100101100101")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 2)
            self.assertEqual(self.word_count, 3)
            self.assertEqual(self.char_count, 0)

    def test_file_with_no_space(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("HiThisIsRichieWhoLovesProgramming,EspeciallyLow-LevelProgrammingAndVintageComputing.")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 0)
            self.assertEqual(self.word_count, 1)
            self.assertEqual(self.char_count, 81)

    def test_file_with_only_newline(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("\n")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 1)
            self.assertEqual(self.word_count, 0)
            self.assertEqual(self.char_count, 0)

    def test_file_with_only_tab(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write("\t")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 0)
            self.assertEqual(self.word_count, 0)
            self.assertEqual(self.char_count, 0)

    def test_file_with_only_space(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as temp_file:
            temp_file.write(" ")
            temp_file.seek(0)

            self.line_count, self.word_count, self.char_count = file_processor(temp_file.name)

            self.assertEqual(self.line_count, 0)
            self.assertEqual(self.word_count, 0)
            self.assertEqual(self.char_count, 0)


if __name__ == '__main__':
    unittest.main()
