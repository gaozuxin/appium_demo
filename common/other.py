import os
from common.myLogger import logger


def fail_run(n=2):
    def decorator(func):
        def wrapper(*args,**kw):
            for i in range(n):
                try:
                    r = func(*args,**kw)
                    return r
                except Exception as err:
                    logger.error('[{}]用例第{}次失败原因{}'.format(os.path.basename(__file__), i+1, err))
            raise Exception
        return wrapper
    return decorator
