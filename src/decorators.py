import functools
import logging


def log(filename=None):
    """
    Декоратор для логирования функции, а также просмотра ее результатов/ошибок.
    Этот декоратор записывает информацию о вызовах обернутой функции, переданные
    аргументы и возвращаемое значение.
    В случаи ошибки, так же записывается информация об ошибке
    """

    logger = logging.getLogger("mylog.txt")#(__name__)

    if filename:
        handler = logging.FileHandler(filename)
        logger.addHandler(handler)
    else:
        handler = logging.StreamHandler()
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Логиреум начало работы функции
                logger.info(f"Starting {func.__name__} with args: {args} kwargs: {kwargs}")
                print(f"Starting {func.__name__} with args: {args} kwargs: {kwargs}")

                result = func(*args, **kwargs)

                # Логируем успешное окончание работы функции
                logger.info(f"{func.__name__} ok: Result: {result}")
                print(f"{func.__name__} ok: Result: {result}")
                return result

            except Exception as e:
                # Логируем ошибку
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator

# Пример использования декоратора
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y