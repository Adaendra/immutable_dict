import unittest

from src.immutable_dict.ImmutableDict import ImmutableDict


def test_creation_empty():
    immutable_dict = ImmutableDict({})

    assert immutable_dict is not None
    assert immutable_dict.__class__ == ImmutableDict
    assert len(immutable_dict) == 0


def test_creation_not_empty():
    immutable_dict = ImmutableDict({"hello": "world"})

    assert immutable_dict is not None
    assert immutable_dict.__class__ == ImmutableDict
    assert len(immutable_dict) == 1
    assert immutable_dict["hello"] == "world"


def test_creation_inception():
    immutable_dict = ImmutableDict(ImmutableDict({"hello": "world"}))

    assert immutable_dict is not None
    assert immutable_dict.__class__ == ImmutableDict
    assert len(immutable_dict) == 1
    assert immutable_dict["hello"] == "world"


if __name__ == '__main__':
    unittest.main()
