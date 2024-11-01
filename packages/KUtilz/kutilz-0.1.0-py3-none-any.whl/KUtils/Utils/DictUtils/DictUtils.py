from typing import List, Any, TypeVar, Dict, Callable

V = TypeVar('V')
K = TypeVar('K')
T = TypeVar('T')

def make_dicts(keys: List[str], vals: List[List[Any]])->dict:
    assert all([len(keys) == len(sub_vals) for sub_vals in vals])
    
    res = []
    for sub_val in vals:
        new_item = {}
        for i, key in enumerate(keys):
            new_item[key] = sub_val[i]

        res.append(new_item)
    return res

def merge(dict0: dict, dict1: dict)->dict:
    if not dict0: return dict1
    if not dict1: return dict0

    return dict0.update(dict1)

def set_chained(dict: dict, keys: List[str], val: Any)->None:
    next = dict
    for key in keys[:-1]:
        if not key in next:
            next[key] = {}

        next = next[key]

    next[keys[-1]] = val

def get_chained(dict: dict, keys: List[str])->Any:
    next = dict
    for key in keys[:-1]:
        next = next[key]

    return next.get(keys[-1])

def auto_dict(*args)->dict:
    return dict({arg:eval(arg) for arg in args})

def vmap(d: Dict[K, V], func: Callable[[K], T])-> Dict[K, T]:
    return {
        key: func(val) for key, val in d.items()
    }

def notin(a: dict, b: dict)->dict:
    return {
        key: val for key, val in a.items if key not in b.keys()
    }

