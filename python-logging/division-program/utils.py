import logging

logger = logging.getLogger(__name__)


def devide(x: float, y: float) -> float:
    """
    Devide `x` by `y` and log the process.

    Arguments:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If `y` is zero.
        TypeError: If inputs are not numbers.
    """

    logger.debug("Attempting to devide {} by {}".format(x, y))

    try:
        result = x / y
        logger.info("Devision successfull: {} / {} = {}".format(x, y, result))
        return result

    except ZeroDivisionError as e:
        logger.exception("Division by zero error.")
        logger.info("-" * 40)
        # Re-raise the cought exception
        raise

    except TypeError as e:
        logger.exception("Invalid input type.")
        logger.info("-" * 40)
        # Re-raise the cought exception
        raise
