from __future__ import annotations

import pathlib
from pathlib import Path
import typing
from typing import (
                    List,
                    Union,
                    Optional,
                    Tuple,
                    Any,
                    Callable,
                    Dict,
                    OrderedDict,
                    Type,
                    Generic,
                    Protocol,
                    Mapping,
                    Iterator,
                    Iterable,
                    Literal,
                    cast)

from typing_extensions import (ParamSpec,
                               Concatenate,
                               Self,
                               TypeVar,
                               Set,
                               TypeAlias,
                               TypedDict,
                               TypeVarTuple,
                               Unpack,
                               TYPE_CHECKING,
                               NamedTuple,
                               Annotated,
                               NotRequired,
                               overload,
                               override)
from functools import update_wrapper
from numbers import Number
import abc


IParams = Dict[str, Any]

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K')
V = TypeVar('V')
P = ParamSpec('P')
Ts = TypeVarTuple('Ts')
NormalizedColor = TypeVar('NormalizedColor', bound=Tuple[float, float, float])

# PathLike = TypeVar('PathLike', pathlib.Path, str, covariant=True)
PathLike = Union[Path, str]
JObject = Dict[str, Union[str, Any]]

# PathOrContent = Union[PathLike, Generic[T]]
JSONPoC = Union[PathLike, JObject]

class Fuck(Exception): pass