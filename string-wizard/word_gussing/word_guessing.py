from random import sample as random_generator


LETTERS = "abcdefghij"

def word_generator() -> str:
    """
    Generating a random word with the expected letters defined
    as a static variable named LETTERS.
    """
    generated_word = "".join(random_generator(LETTERS, 5))
    return generated_word
