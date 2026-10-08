import logging
from random import sample as random_generator

from utils.logging_conf import base_logger

logger = logging.getLogger("WORD GUESSING")
base_logger(logger)


LETTERS = "abcdefghij"

def word_generator() -> str:
    """
    Generating a random word with the expected letters defined
    as a static variable named LETTERS.
    """
    generated_word = "".join(random_generator(LETTERS, 5))
    return generated_word

def user_guesses(enter_time_limit: int, character_length_limit: int) -> str:
    """
    Getting user input 'n' times which 'n' provided by
    function arguments which is 'enter_time_limit'.

    Raising values error if the values does not equal
    to the defined character limit which provided
    by function arguments which is 'character_length_limit'.

    Arguments:
        enter_time_limit (int): The times user be able to enter a guess.
        character_length_limit (int): Length of characters user guess should have.
    """
    _user_guess = str()
    _guesses = set()
    _entered_num = 0

    print(f"\nYour guess word should be equivalent to {character_length_limit} characters.")
    print(f"You have {enter_time_limit} times to guess.\n")
    while _entered_num <  enter_time_limit:
        try:
            _user_guess = input("What is your guess: ")

            if len(_user_guess) == character_length_limit:
                _entered_num += 1
                _guesses.add(_user_guess)
            else:
                logger.exception("Value error occurred in the length of guess.")
                raise ValueError(
                    f"The entered guess did not equivalent to {character_length_limit} characters."
                )

        except EOFError as eof_error:
            logger.exception(eof_error)
            # Re-raise occurred exception
            raise

        except Exception as occurred_exception:
            logger.exception(occurred_exception)
            # Re-raise occurred exception
            raise

    logger.debug("User guesses are '%s'", _guesses)
    return _guesses


def words_checker(guesses: set) -> dict:
    """
    Checks the words client entered with the generated word by program.

    If any of user guesses identically equal to the generated word,
    the client succeed to guess correctly, otherwise:
        - if user guess's all letters not equal to generated word's all letter.
        - if user guess's all letters correct but
            not in the correct position of generated word's letters position.
    then user guessed wrong.

    Arguments:
        guesses (set): The guesses client entered.
    """
    found_number = 0
    correct_index = 0
    guesses_result = {}

    generated_word = word_generator()
    logger.info(generated_word)

    # Go through the client guesses to compare with the generated word
    for guess in guesses:
        # Checks if the current letter of generated word
        # inside the current guess word to increase the found-number
        for index_num, word in enumerate(generated_word):
            if word in guess:
                found_number += 1

            # Checks the equivalent of the current guess letter
            # and the current generated word letter
            if guess[index_num] == generated_word[index_num]:
                correct_index += 1

        # Fill the result with the current guess as key
        # and its found-number with its correct-index as its value
        guesses_result[guess] = f"{found_number} {correct_index}"

        # Reset found number for the next guess word
        found_number = 0
        correct_index = 0

    return guesses_result
