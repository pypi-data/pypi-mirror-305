from functools import wraps
from time import time

def timeit(rep: int = 1):
    def _timeit(f):
        @wraps(f)
        def wrap(*args, **kw):
            ts = time()
            for _ in range(rep):
                result = f(*args, **kw)
            te = time()

            t_total = te - ts
            t_per = (te - ts) / rep

            print(f'{f.__name__} took {t_total:.4} to run {rep} times, {t_per:.4}/rep')

            return result
        return wrap
    return _timeit