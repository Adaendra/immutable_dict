import unittest

from src.immutable_dict.ImmutableDict import ImmutableDict

# --- Copy
def test_copy():
    immutable_dict = ImmutableDict({"hello": "world"})
    immutable_dict2 = immutable_dict.copy()

    assert immutable_dict2 is not None
    assert immutable_dict2.__class__ == ImmutableDict
    assert immutable_dict == immutable_dict2
    assert len(immutable_dict) == 1


def test_copy_internal():
    immutable_dict = ImmutableDict({"hello": "world"})
    immutable_dict2 = immutable_dict.__copy__()

    assert immutable_dict2 is not None
    assert immutable_dict2.__class__ == ImmutableDict
    assert immutable_dict == immutable_dict2
    assert len(immutable_dict) == 1


# --- From Keys
def test_fromkeys_from_instance():
    other_instance = ImmutableDict({"hello": "world"})
    immutable_dict = other_instance.fromkeys(["a", "b"], "1")

    assert immutable_dict is not None
    assert immutable_dict.__class__ == ImmutableDict
    assert len(immutable_dict) == 2
    assert immutable_dict["a"] == "1"
    assert immutable_dict["b"] == "1"


def test_fromkeys_static():
    immutable_dict = ImmutableDict.fromkeys(["a", "b"], "1")

    assert immutable_dict is not None
    assert immutable_dict.__class__ == ImmutableDict
    assert len(immutable_dict) == 2
    assert immutable_dict["a"] == "1"
    assert immutable_dict["b"] == "1"


if __name__ == '__main__':
    unittest.main()
