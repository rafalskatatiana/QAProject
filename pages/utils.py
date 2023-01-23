import datetime
import logging
import random
import string
from time import sleep


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.25):
    """Retires function until ok (or 5 seconds)"""
    log = logging.getLogger("[Wait until OK]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catch: {err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    sleep(period)

        return wrapper

    return decorator
