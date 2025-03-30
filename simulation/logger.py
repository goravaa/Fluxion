# simulation/logger.py
import functools
import logging

# Configure basic logging; adjust as needed.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with args: {args[1:]}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Completed {func.__name__}")
        return result
    return wrapper
