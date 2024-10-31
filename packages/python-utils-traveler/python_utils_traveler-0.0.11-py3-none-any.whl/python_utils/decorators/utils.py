import time
from functools import wraps

from python_utils.logging.logging import init_logger

logger = init_logger()

def timeit(fn):
    '''
    Description: decorator function that times the functions process time

    Args:
        - fn: the function being passed
    '''
    def get_time(*args, **kwargs): 
        start = time.time() 
        output = fn(*args, **kwargs)
        logger.info(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time

def timeit_async(fn):
    '''
    Description: decorator function that times the functions process time

    Args:
        - fn: the function being passed
    '''
    @wraps(fn)
    async def get_time(*args, **kwargs): 
        start = time.time() 
        output = await fn(*args, **kwargs)
        logger.info(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time 