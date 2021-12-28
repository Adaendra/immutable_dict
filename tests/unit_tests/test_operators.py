import unittest
from operator import ior

from src.immutable_dict.ImmutableDict import ImmutableDict


def test_or():
    immutable_dict_1 = ImmutableDict({"a": "1"})
    immutable_dict_2 = ImmutableDict({"b": "2"})

    result = immutable_dict_1 | immutable_dict_2

    assert result is not None
    assert result == immutable_dict_1
    assert result != immutable_dict_2


def test_ior():
    immutable_dict_1 = ImmutableDict({"a": "1"})
    immutable_dict_2 = ImmutableDict({"b": "2"})

    result = ior(immutable_dict_1, immutable_dict_2)

    assert result is not None
    assert result == immutable_dict_1
    assert result != immutable_dict_2



if __name__ == '__main__':
    unittest.main()
