import unittest

from src.adaendra_immutable_dict.AdaendraImmutableDict import AdaendraImmutableDict


def test_creation_empty():
    immutable_dict = AdaendraImmutableDict({})

    assert immutable_dict is not None
    assert immutable_dict.__class__ == AdaendraImmutableDict
    assert len(immutable_dict) == 0


def test_creation_not_empty():
    immutable_dict = AdaendraImmutableDict({"hello": "world"})

    assert immutable_dict is not None
    assert immutable_dict.__class__ == AdaendraImmutableDict
    assert len(immutable_dict) == 1
    assert immutable_dict["hello"] == "world"


def test_creation_inception():
    immutable_dict = AdaendraImmutableDict(AdaendraImmutableDict({"hello": "world"}))

    assert immutable_dict is not None
    assert immutable_dict.__class__ == AdaendraImmutableDict
    assert len(immutable_dict) == 1
    assert immutable_dict["hello"] == "world"


if __name__ == '__main__':
    unittest.main()
