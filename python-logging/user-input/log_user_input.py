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

    Returns:
        string: Reports user has just logged in.
    """

    first_name = first_name.title()
    last_name = last_name.title()
    username = username.lower()

    return "User with \"{}\" username just logged in.".format(username)


def main():
    """
    Main function will run the program when call it.

    Handle exceptions and inputs. Logs the occured exceptions and other program parts.
    """

    logging.info("Program started.")

    fname_input = lname_input = username_input = "Unknown"

    try:
        fname_input = input("Enter your first name please: ")
        lname_input = input("Enter your last name please: ")
        username_input = input("Enter your username please: ")

        logging.info("Received user information.")
        logging.info("-" * 40)

    except EOFError as e:
        logging.exception("End of file error. No input received.")
        logging.info("-" * 40)
        # Re-raise the cought exception
        raise

    except Exception as e:
        logging.exception("An unexpected error occured: {e}".format(e))
        logging.info("-" * 40)
        # Re-raise the cought exception
        raise

    # Check inputs if each of them is NULL, then set it as a 'Unknown'
    first_name = fname_input.title() or "Unknown"
    last_name = lname_input.title() or "Unknown"
    username = username_input.lower() or "Unknown"

    # Logs the `user` function
    logging.info(user(first_name, last_name, username))

    logging.info(
        "User with \"{}\" firstname, \"{}\" lastname, and \"{}\" username has just logged in.".format(first_name, last_name, username)
    )
    logging.info("-" * 40)


if __name__ == '__main__':
    main()
