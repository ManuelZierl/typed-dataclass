from dataclasses import dataclass, fields, is_dataclass

from typeguard import check_type, CollectionCheckStrategy


def typed_dataclass(cls: dataclass) -> dataclass:
    """
    A decorator for Python dataclasses to enable runtime type checking.

    This decorator should be used in conjunction with the @dataclass decorator
    and should be placed below @dataclass. The correct usage is:

    @dataclass
    @typed_dataclass
    class MyClass:
        my_field: int

    Wraps the dataclass's __post_init__ method to check the type of each field
    after object initialization.
    """
    original_post_init = getattr(cls, "__post_init__", None)

    def __post_init_with_type_checks(self):
        if hasattr(cls, "__before_type_check__"):
            cls.__before_type_check__(self)
        for field in fields(cls):
            check_type(getattr(self, field.name), field.type,collection_check_strategy=CollectionCheckStrategy.ALL_ITEMS)
        if original_post_init:
            original_post_init(self)

    setattr(cls, "__post_init__", __post_init_with_type_checks)
    return cls
