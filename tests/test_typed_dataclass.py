import unittest
from dataclasses import dataclass
from typing import List, Optional, Union

from typeguard import TypeCheckError

from src.typed_dataclass import typed_dataclass


class TestTypedDataclass(unittest.TestCase):
    @dataclass
    @typed_dataclass
    class TestClass:
        number: int
        str_list: List[str]
        int_or_str: Union[int, str]
        optional: Optional[float] = None

    @dataclass
    @typed_dataclass
    class TestClassWithPostInit:
        number: int
        str_list: List[str]
        int_or_str: Union[int, str]
        optional: Optional[float] = None

        def __post_init__(self):
            self.number = 1

    def test_correct_types(self):
        try:
            c1 = self.TestClass(10, ["hello"], 1)
            assert c1.number == 10
            assert c1.str_list == ["hello"]
            assert c1.int_or_str == 1
            c2 = self.TestClass(10, ["hello", "world"], "string", 5.6)
            assert c2.number == 10
            assert c2.str_list == ["hello", "world"]
            assert c2.int_or_str == "string"
            c = self.TestClassWithPostInit(10, ["hello", "world"], "string", 5.6)
            assert c.number == 1
        except TypeCheckError:
            self.fail("TypeCheckError raised unexpectedly!")

    def test_incorrect_types(self):
        with self.assertRaises(TypeCheckError):
            self.TestClass("10", ["hello"], 1)

        with self.assertRaises(TypeCheckError):
            self.TestClass("10", ["hello"], 1)

        with self.assertRaises(TypeCheckError):
            self.TestClass(1, ["hello"], 1, "0")

    def test_before_type_check(self):
        @dataclass
        @typed_dataclass
        class TestClassWithBeforeTypeCheck:
            number: int

            def __before_type_check__(self):
                self.number = int(self.number)

            def __post_init__(self):
                self.number += 1

        assert TestClassWithBeforeTypeCheck("1").number == 2


if __name__ == "__main__":
    unittest.main()
