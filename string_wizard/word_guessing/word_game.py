import random


WORDS = ["book", "sea", "linux", "python", "golang", "math", "django", "data"]


def word_selector(words: list[str]) -> tuple[int, str, str]:
	"""
	Choosing a word in the list of words provided by function.
	
	Arguments:
		words (list[str]): List of words should choose between them.
	"""
	word = random.choice(words)
	word_length = "-" * len(word)
	
	return (len(word), word_length, word)

def word_game(limit_num: int=None) -> str:
	"""
	The main game management. Generate a word from the "word selector"
	function and checks character by character with what user guesses,
	handling the limitation of user guesses which provided by the function args.
	
	Arguments:
		limit_num (int): The limitation for user maximum guesses.
	"""
	word = word_selector(words=["book"]).lower()
	hidden = list(word[1])
	limit_num = word[0] if not limit_num else limit_num
	guess_counter = 0

	# Shows the length of the generated word with < - > .
	print("".join(hidden))

	while guess_counter < limit_num:
		if "".join(hidden) == word[2]:
			break

		if len(user_guess) != 1:
		    continue

		user_guess = input("Enter your guess character: ").lower()
		for num, char in enumerate(word[2]):
			if user_guess == char:
				hidden[num] = user_guess

		# Prints the output and the correctness of user guess character
		# place per sending a character
		print("".join(hidden))

		guess_counter += 1

	if "".join(hidden) == word[2]:
		return "You WON :)"
	else:
		return "Try again, you can WIN :)"


def main():
	try:
		user_guess_limit = int(input("Enter the guess limitation you consider: "))

		return word_game(limit_num=user_guess_limit)
		
	except EOFError:
		print("EOFError occurred.")

	except ValueError:
		print("The limitation number should only contains Digits")

	except KeyboardInterrupt:
		print("Keyboard interuppt exception occurred.")


if __name__ == "__main__":
	print(main())
