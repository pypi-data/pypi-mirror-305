import numpy as np
from KUtils.Typing import *

ArrayLike = Union[List, np.ndarray]

def flattend(array: ArrayLike) -> List:
    return np.array(array).reshape(-1).tolist()