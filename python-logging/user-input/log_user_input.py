import logging

logging.basicConfig(
    filename="user_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def user(first_name: str, last_name: str, username: str) -> str:
    """
    Gets the users info and return their username.

    Arguments:
        first_name (str): User's first name. Converts it to a title case.
        last_name (str): User's last name. Converts it to a title case.
        username (str): User's username. Converts it to a lower case.

    Return:
        Return a string to say user has just logged in with its username.
    """

    first_name = first_name.title()
    last_name = last_name.title()
    username = username.lower()

    return "User with \"{}\" username just logged in.".format(username)


def main():
    logging.info("Program started.")


if __name__ == '__main__':
    main()
