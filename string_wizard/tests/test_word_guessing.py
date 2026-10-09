import logging
from unittest import TestCase, main
from unittest.mock import patch, PropertyMock

from string_wizard.word_guessing.word_guessing import WordGuessing


class TestWordGenerator(TestCase):
    """
    Test cases for the word generator method in Word Guessing class.
    """
    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)

    def setUp(self):
        """
        Setting-up an initialization of the class to use in the test cases.
        """
        self.word_guessing = WordGuessing("abcdefghj", 5)

    def test_word_generator(self):
        """
        Testing the word generator method which should generate
        a word according to the character limit passed to function.
        """
        generated_word = self.word_guessing.word_generator

        self.assertEqual(len(generated_word), 5)
        self.assertEqual(type(generated_word), str)

class TestUserGuesses(TestCase):
    """
    Test cases for User Guesses which includes the user inputs and handle them
    in the Word Guessing class.
    """
    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)

    def setUp(self):
        """
        Setting-up an initialization of the class to use in the test cases.
        """
        self.word_guessing = WordGuessing("abcdefghj", 5)

    def test_return_all_valid_guesses(self):
        """
        Tests the user guesses method to ensure it returns all valid guesses
        which passed to function by client.
        """
        with patch("builtins.input", side_effect=["abcde", "fghjc", "ehbcd"]):
            word_guesses = self.word_guessing.user_guesses(
                enter_time_limit=3,
                character_length_limit=5
            )

        self.assertIn("abcde", word_guesses)
        self.assertIn("fghjc", word_guesses)
        self.assertIn("ehbcd", word_guesses)

    def test_raised_value_error(self):
        """
        Tests it raises the value error on wrong length.
        Checks whether it raises Value Error on bigger or less than 'character-length-limit'.
        """
        with patch("builtins.input", side_effect=["abcde", "jhdfa", "ed"]):
            with self.assertRaises(ValueError):
                self.word_guessing.user_guesses(
                    enter_time_limit=3,
                    character_length_limit=5
                )

        with patch("builtins.input", side_effect=["abcdef", "jhdfa", "edfch"]):
            with self.assertRaises(ValueError):
                self.word_guessing.user_guesses(
                    enter_time_limit=3,
                    character_length_limit=5
                )

    def test_raised_eof_error(self):
        """
        Tests it raises the EOFError in the situation.
        """
        with patch("builtins.input", side_effect=EOFError):
            with self.assertRaises(EOFError):
                self.word_guessing.user_guesses(
                    enter_time_limit=3,
                    character_length_limit=5
                )

    def test_duplicated_guesses(self):
        """
        Tests that the result does not contain any duplicated value.
        """
        with patch("builtins.input", side_effect=["abcde", "abcde", "jhgbe"]):
            word_guesses = self.word_guessing.user_guesses(
                enter_time_limit=3,
                character_length_limit=5
            )

            self.assertEqual(list(word_guesses).count("abcde"), 1)


class TestWordChecker(TestCase):
    """
    Test cases for the word checker method in Word Guessing class.
    """
    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)

    def setUp(self):
        self.word_guessing = WordGuessing(characters="abcdefghij", word_length=5)

    def test_result_match(self):
        """
        Tests the exact result of the word checker function, the expected result.
        """
        with patch.object(
            WordGuessing, "word_generator",
            new_callable=PropertyMock,
            return_value="abcde"
        ):
            result = self.word_guessing.words_checker({"abcde"})

        self.assertEqual(result, {"abcde": "5 5"})

    def test_right_letters_wrong_position(self):
        """
        Tests the right letters but wrong position/index.
        """
        with patch.object(
            WordGuessing, "word_generator",
            new_callable=PropertyMock,
            return_value="abcde"
        ):
            result = self.word_guessing.words_checker({"edcab"})

        self.assertEqual(result, {"edcab": "5 1"})


if __name__ == "__main__":
    main()
