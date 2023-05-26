# Typed Dataclass

Typed Dataclass is a Python library providing a decorator for dataclasses that enables runtime type checking.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install typed-dataclass.

> pip install typed-dataclass

## Usage

This library should be used in conjunction with the `@dataclas` decorator and should be placed
below `@dataclass`. On object initialization it checks types by using
[typeguard](https://github.com/agronholm/typeguard) package. Internally this works by modifying 
the `__post__init__` method of the dataclass.

```python
from dataclasses import dataclass
from typed_dataclass import typed_dataclass

@dataclass
@typed_dataclass
class MyClass:
    my_field: int

MyClass(12)   # will succeed
MyClass ("a") # will fail
```

### Pre Validation

You can also implement logic that is happening before Type checks defining `__before_type_check__` function:

```python
from dataclasses import dataclass
from typed_dataclass import typed_dataclass

@dataclass
@typed_dataclass
class MyClass:
    my_int: int
    
    def __before_type_check__(self):
        self.my_int = int(self.my_int)

```

## Testing
> python -m unittest discover tests


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)