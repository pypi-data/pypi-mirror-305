from KUtils.Typing import *

def generic_args(cls: type) -> List[Any]:
    try:
        orig_bases = cls.__orig_bases__
    except AttributeError:
        orig_bases = [cls]
    params = []
    for base in orig_bases:
        params.extend([*typing.get_args(base)])
    return params


def force_list(obj: Union[T, List[T]]) -> List[T]:
    if isinstance(obj, list):
        return obj
    else:
        return [obj]
    
from importlib import import_module
def from_import(module_res: str, obj_name: str, default=None, local=False)->Any:
    module = import_module(module_res, package='.' if local else None)
    return getattr(module, obj_name, default)


def Mapper(keys: Generic[K], items: List[T]) -> Dict[K, T]:
    gen_args = generic_args(keys)
    assert len(gen_args) == len(items)

    return dict(zip(gen_args, items))