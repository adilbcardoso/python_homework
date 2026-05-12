import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(logging.FileHandler("./decorator.log","a"))
...
# To write a log record:
#logger.log(logging.INFO, "this string would be logged")
def logger_decorator (func):
    @wraps (func)
    def wrapper (*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")

        if args:
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else: 
            logger.log(logging.INFO, "positional parameters: none")

        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else: 
            logger.log(logging.INFO, "keyword parameters: none")

        result = func(*args, **kwargs)

        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "-" * 40)

        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def check_args(*args):
    return True

@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    check_args(1, 2, 3, "test")
    keyword_only(name="Adilson", course="Python", level=3)



