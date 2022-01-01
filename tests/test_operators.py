import unittest
from operator import ior

from src.adaendra_immutable_dict.AdaendraImmutableDict import AdaendraImmutableDict


def test_or():
    immutable_dict_1 = AdaendraImmutableDict({"a": "1"})
    immutable_dict_2 = AdaendraImmutableDict({"b": "2"})

    result = immutable_dict_1 | immutable_dict_2

    assert result is not None
    assert result == immutable_dict_1
    assert result != immutable_dict_2


def test_ior():
    immutable_dict_1 = AdaendraImmutableDict({"a": "1"})
    immutable_dict_2 = AdaendraImmutableDict({"b": "2"})

    result = ior(immutable_dict_1, immutable_dict_2)

    assert result is not None
    assert result == immutable_dict_1
    assert result != immutable_dict_2


if __name__ == '__main__':
    unittest.main()
