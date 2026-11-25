import random


def word_selector(words: list[str]) -> tuple:
	"""
	Choosing a word in the list of words provided by function.
	
	Arguments:
		words (list[str]): List of words should choose between them.
	"""
	word = random.choice(words)
	word_length = "-" * len(word)
	
	return (len(word), word_length, word)

