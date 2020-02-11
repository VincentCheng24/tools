from functools import wraps


# Define a class with a singleton instance.
def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


# Counting Recursive Function Calls with Decorators
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper


def timing(func):
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):

        st = time.time()
        res = func(*args, **kwargs)
        print('Function {}() costs {:.4f} sec'.format(func.__name__, time.time()-st))
        return res

    return wrapper


