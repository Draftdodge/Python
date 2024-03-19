import logging
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}. В функции {funcName} {msg}'
logging.basicConfig(format=FORMAT, filename='Student.log', encoding='utf-8', style='{', level=logging.NOTSET)

def log_decorator(func):
    logger = logging.getLogger(__name__)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug(f'{args} {kwargs} {res}')
        return res
    return wrapper