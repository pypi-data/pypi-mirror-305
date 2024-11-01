import functools
import typing

from pydantic import (ConfigDict,
                      BaseModel,
                      Field, computed_field, TypeAdapter, model_validator, field_validator, ValidationError,
                      ValidatorFunctionWrapHandler,
                      Discriminator, Tag,
                      field_serializer
                      )
from pathlib import Path
from typing import Union, List, Set, Generic
from typing_extensions import NotRequired, Self, Type, TypedDict, Unpack, Any, Literal, Optional, Dict, TypeVar, Annotated, ClassVar

DerivedDataClass = TypeVar('DerivedDataClass', default='DataClass')

import yaml
import json

Extra = Annotated[Dict, Field(default_factory=dict)]
SerializableTags = Annotated[List[str], Field(default=None)]

class DumpArgs(TypedDict):
    include: NotRequired[Any]
    exclude: NotRequired[Any]
    mode: NotRequired[Literal['json', 'python']]
    exclude_unset: NotRequired[bool]
    exclude_defaults: NotRequired[bool]
    exclude_none: NotRequired[bool]
    serialize_as_any: NotRequired[bool]


def generate_class_identifier(cls, cutoff=None):
    mro = cls.mro()
    identifier = []
    for base in mro:
        identifier.append(base.__name__)
        if cutoff and base.__name__ == cutoff:
            break
    return ".".join(identifier)


def gen_class_ident(cls: type) -> str:
    return cls.__name__.lower()

class DataClass(BaseModel):
    __polymorphs__: ClassVar[bool] = False
    __subs__: ClassVar[Dict[str, Self]] = None
    __hashable__: ClassVar[bool] = None
    __parentdataclass__: ClassVar[Type[Self]]

    poly_adaptor: ClassVar[TypeAdapter]

    model_config = ConfigDict(extra='forbid',
                              use_enum_values=True)

    subtype: Annotated[str, Field(default=None, exclude=True)]
    uhid: Annotated[str, Field(default=None, exclude=True)]

    @classmethod
    def BANDAID_get_subtype(cls) -> str:
        return cls.model_fields['subtype'].default

    @model_validator(mode='wrap')
    @classmethod
    def __parse_into_subclass(cls, v: Any, handler: ValidatorFunctionWrapHandler) -> Self:
        if cls.__polymorphs__ and cls.poly_adaptor is not None:
            return cls.poly_adaptor.validate_python(v)
        return handler(v)

    def __init_subclass__(cls, **kwargs):
        ident = gen_class_ident(cls)
        cls.model_fields['subtype'].default = ident

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        needs_rebuild = False

        cls.__subs__ = {}

        base_class = cls.__base__

        if not issubclass(base_class, DataClass):
            return

        #DEAL WITH SUBTYPES
        cls.__parentdataclass__ = base_class

        ident = gen_class_ident(cls)

        base_class.__subs__ = base_class.__subs__ or {}

        base_class.__subs__[ident] = cls

        def update_graph(clas: 'DataClass'):
            if not issubclass(clas, DataClass):
                return

            if not clas.__polymorphs__:
                return

            clas.model_fields['subtype'].exclude = False
            variants = [*clas.__subs__.values()]
            if len(variants) > 1:
                adaptor = TypeAdapter(
                    Annotated[Union[tuple(
                        Annotated[sub, Tag(gen_class_ident(sub))] for sub in variants
                    )], Discriminator(lambda x: dict(x)['subtype'])]
                )
            elif len(variants) > 0:
                adaptor = TypeAdapter(variants[0])
            else:
                adaptor = None

            clas.poly_adaptor = adaptor

        update_graph(base_class)
        update_graph(cls)

        #todo: PLEASE FUCKINGG GET RID OF THIS SHIT
        grandparent = getattr(base_class, '__parentdataclass__', None)
        if grandparent is not None:
            if '[' in gen_class_ident(base_class) or grandparent.__polymorphs__:
                grandparent.__subs__[ident] = cls
                update_graph(grandparent)

        #DEAL WITH HASHABILITY
        if cls.__hashable__ is True:
            if cls.model_fields['uhid'].exclude == True:
                cls.model_fields['uhid'].exclude = False
                needs_rebuild = True

        if needs_rebuild:
            cls.model_rebuild(force=True)

    @classmethod
    def deserialize(cls, serialized: Dict[str, Any]) -> Self:
        return cls(**serialized)

    @classmethod
    def default_of(cls, key: str) -> Any:
        field_info = cls.model_fields[key]
        return field_info.default

    @classmethod
    def build_default(cls) -> Self:
        return cls()

    @classmethod
    def from_yaml(cls, path: Union[Path, str]) -> Self:
        with open(path, 'r') as file:
            y = yaml.safe_load(file)

        return cls(**y)

    def to_dict(self, **dumpargs: Unpack[DumpArgs]) -> Dict[str, Any]:
        dumpargs = dumpargs or {}
        dumpargs.setdefault('include', None)
        dumpargs.setdefault('exclude', None)
        dumpargs.setdefault('mode', 'json')
        dumpargs.setdefault('exclude_unset', False)
        dumpargs.setdefault('exclude_none', True)
        dumpargs.setdefault('exclude_defaults', False)
        dumpargs.setdefault('serialize_as_any', True)
        return self.model_dump(**dumpargs)

    def stringify(self, **dumpargs: Unpack[DumpArgs]) -> str:
        return json.dumps(self.to_dict(dumpargs))

    def to_yaml(self, path: Union[Path, str], **dumpargs: Unpack[DumpArgs]) -> None:
        serialized = self.to_dict(**dumpargs)

        with open(path, 'w') as file:
            yaml.dump(serialized, file)

    @field_serializer('tags', check_fields=False)
    def __serialize_tags(self, v: Union[List[str], Set[str]]):
        return ','.join(v)

    @field_validator('tags', mode='before', check_fields=False)
    @classmethod
    def __validate_tags(cls, v: Union[List[str], Set[str], str]):
        if isinstance(v, str):
            v = v.split(',')
        return list(set(v))

    def freeze(self) -> None:
        pass

    def compute_hash(self) -> str:
        raise NotImplementedError(f'Object {self.__class__} has no hashable implementation!')

    def hash_n_set(self) -> str:
        assert 'uhid' in self.__class__.model_fields
        assert self.uhid is None
        self.uhid = self.compute_hash()
        return self.uhid

    def get_hash(self) -> str:
        assert 'uhid' in self.__class__.model_fields
        return self.uhid or self.hash_n_set()

    def reduce_to(self, other: Type['DataClass']) -> 'DataClass':
        keys = other.model_fields.keys()
        me = self.to_dict()


        inst = other(**{
            key: me[key] for key in keys if key in me
        })

        return inst

def generic_dataclass_builder():
    import inspect
    code = inspect.getsource(DataClass)
    code = code.replace('DataClass', 'GenericDataClass')
    code = code.replace('GenericDataClass(BaseModel)', 'GenericDataClass(BaseModel, Generic[_PLACEHOLDER])')
    return functools.partial(exec, code)

DerivedGenericDataClass = TypeVar('DerivedGenericDataClass')
_PLACEHOLDER = TypeVar('_PLACEHOLDER')
generic_dataclass_builder()()
if typing.TYPE_CHECKING:
    GenericDataClass = DataClass

# class GenericDataClass(BaseModel, Generic[_PLACEHOLDER]):
#     __polymorphs__: ClassVar[bool] = False
#     __subs__: ClassVar[Dict[str, Self]] = None
#     __parentdataclass__: ClassVar[Type[Self]]
#
#     poly_adaptor: ClassVar[TypeAdapter]
#
#     model_config = ConfigDict(extra='forbid',
#                               use_enum_values=True)
#
#     subtype: Annotated[str, Field(default='error', exclude=True)] = 'error'
#
#     @classmethod
#     def BANDAID_get_subtype(cls) -> str:
#         return cls.model_fields['subtype'].default
#
#     @model_validator(mode='wrap')
#     @classmethod
#     def __parse_into_subclass(cls, v: Any, handler: ValidatorFunctionWrapHandler) -> Self:
#         if cls.__polymorphs__:
#             if (poly_adaptor := getattr(cls, 'poly_adaptor', None)) is not None:
#                 return poly_adaptor.validate_python(v)
#         return handler(v)
#
#     def __init_subclass__(cls, **kwargs):
#         ident = gen_class_ident(cls)
#         cls.model_fields['subtype'].default = ident
#
#     @classmethod
#     def __pydantic_init_subclass__(cls, **kwargs):
#         cls.__subs__ = {}
#
#         base_class = cls.__base__
#
#         if not issubclass(base_class, GenericDataClass):
#             return
#
#         cls.__parentdataclass__ = base_class
#
#         ident = gen_class_ident(cls)
#
#         base_class.__subs__ = base_class.__subs__ or {}
#
#         base_class.__subs__[ident] = cls
#
#         def update_graph(clas: 'GenericDataClass'):
#             if not issubclass(clas, GenericDataClass):
#                 return
#
#             if not clas.__polymorphs__:
#                 return
#
#             clas.model_fields['subtype'].exclude = False
#             variants = [*clas.__subs__.values()]
#             if len(variants) > 1:
#                 adaptor = TypeAdapter(
#                     Annotated[Union[tuple(
#                         Annotated[sub, Tag(gen_class_ident(sub))] for sub in variants
#                     )], Discriminator(lambda x: dict(x)['subtype'])]
#                 )
#             elif len(variants) > 0:
#                 adaptor = TypeAdapter(variants[0])
#             else:
#                 adaptor = None
#
#             clas.poly_adaptor = adaptor
#
#         update_graph(base_class)
#         update_graph(cls)
#
#
#         #todo: PLEASE FUCKINGG GET RID OF THIS SHIT
#         if '[' in gen_class_ident(base_class):
#             grandparent = base_class.__parentdataclass__
#             grandparent.__subs__[ident] = cls
#             update_graph(grandparent)
#
#     @classmethod
#     def deserialize(cls, serialized: Dict[str, Any]) -> Self:
#         return cls(**serialized)
#
#     @classmethod
#     def default_of(cls, key: str) -> Any:
#         field_info = cls.model_fields[key]
#         return field_info.default
#
#     @classmethod
#     def build_default(cls) -> Self:
#         return cls()
#
#     @classmethod
#     def from_yaml(cls, path: Union[Path, str]) -> Self:
#         with open(path, 'r') as file:
#             y = yaml.safe_load(file)
#
#         return cls(**y)
#
#     def to_dict(self, **dumpargs: Unpack[DumpArgs]) -> Dict[str, Any]:
#         dumpargs = dumpargs or {}
#         dumpargs.setdefault('include', None)
#         dumpargs.setdefault('exclude', None)
#         dumpargs.setdefault('mode', 'python')
#         dumpargs.setdefault('exclude_unset', False)
#         dumpargs.setdefault('exclude_none', True)
#         dumpargs.setdefault('exclude_defaults', False)
#         dumpargs.setdefault('serialize_as_any', True)
#         return self.model_dump(**dumpargs)
#
#     def stringify(self, **dumpargs: Unpack[DumpArgs]) -> str:
#         return json.dumps(self.to_dict(dumpargs))
#
#     def to_yaml(self, path: Union[Path, str], **dumpargs: Unpack[DumpArgs]) -> None:
#         serialized = self.to_dict(dumpargs)
#
#         with open(path, 'w') as file:
#             yaml.dump(serialized, file)
#
#     @field_serializer('tags', check_fields=False)
#     def __serialize_tags(self, v: Union[List[str], Set[str]]):
#         return ','.join(v)
#
#     @field_validator('tags', mode='before', check_fields=False)
#     @classmethod
#     def __validate_tags(cls, v: Union[List[str], Set[str], str]):
#         if isinstance(v, str):
#             v = v.split(',')
#         return list(set(v))
#
#     def freeze(self) -> None:
#         pass
#
#     def compute_hash(self) -> str:
#         raise NotImplementedError(f'Object {self.__class__} has no hashable implementation!')
#
#     def hash_n_set(self) -> str:
#         assert 'uhid' in self.__class__.model_fields
#         assert self.uhid is None
#         self.uhid = self.compute_hash()
#         return self.uhid
#
#     def get_hash(self) -> str:
#         assert 'uhid' in self.__class__.model_fields
#         return self.uhid or self.hash_n_set()
#
#     def reduce_to(self, other: Type[DerivedDataClass]) -> DerivedDataClass:
#         orig_extra = other.model_config['extra']
#         other.model_config['extra'] = 'ignore'
#         inst = other.model_validate(
#             self.to_dict(), strict=True
#         )
#         other.model_config['extra'] = orig_extra
#         return inst