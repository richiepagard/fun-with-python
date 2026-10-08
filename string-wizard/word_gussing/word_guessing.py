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
