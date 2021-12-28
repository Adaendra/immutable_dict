import unittest

from src.adaendra_immutable_dict.AdaendraImmutableDict import AdaendraImmutableDict


# --- Copy
def test_copy():
    immutable_dict = AdaendraImmutableDict({"hello": "world"})
    immutable_dict2 = immutable_dict.copy()

    assert immutable_dict2 is not None
    assert immutable_dict2.__class__ == AdaendraImmutableDict
    assert immutable_dict == immutable_dict2
    assert len(immutable_dict) == 1


def test_copy_internal():
    immutable_dict = AdaendraImmutableDict({"hello": "world"})
    immutable_dict2 = immutable_dict.__copy__()

    assert immutable_dict2 is not None
    assert immutable_dict2.__class__ == AdaendraImmutableDict
    assert immutable_dict == immutable_dict2
    assert len(immutable_dict) == 1


def test_deepcopy():
    immutable_dict = AdaendraImmutableDict({"hello": "world"})
    immutable_dict2 = immutable_dict.__deepcopy__()

    assert immutable_dict2 is not None
    assert immutable_dict2.__class__ == AdaendraImmutableDict
    assert immutable_dict == immutable_dict2
    assert len(immutable_dict) == 1


# --- From Keys
def test_fromkeys_from_instance():
    other_instance = AdaendraImmutableDict({"hello": "world"})
    immutable_dict = other_instance.fromkeys(["a", "b"], "1")

    assert immutable_dict is not None
    assert immutable_dict.__class__ == AdaendraImmutableDict
    assert len(immutable_dict) == 2
    assert immutable_dict["a"] == "1"
    assert immutable_dict["b"] == "1"


def test_fromkeys_static():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    assert immutable_dict is not None
    assert immutable_dict.__class__ == AdaendraImmutableDict
    assert len(immutable_dict) == 2
    assert immutable_dict["a"] == "1"
    assert immutable_dict["b"] == "1"


def test_clear():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.clear()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_pop():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.pop()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_popitem():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.popitem()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_setdefault():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.setdefault()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_update():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.update()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_delattr():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.__delattr__()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_setattr():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.__setattr__()
    except AttributeError as ae:
        # --- Then
        assert ae is not None
        assert ae.args[0] == "'AdaendraImmutableDict' object is read-only"


def test_reduce():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.__reduce__()
    except TypeError as te:
        # --- Then
        assert te is not None
        assert te.args[0] == "'AdaendraImmutableDict' object doesn't support item update"


def test_setitem():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.__setitem__("a", "2")
    except TypeError as te:
        # --- Then
        assert te is not None
        assert te.args[0] == "'AdaendraImmutableDict' object doesn't support item assignment"


def test_delitem():
    immutable_dict = AdaendraImmutableDict.fromkeys(["a", "b"], "1")

    try:
        immutable_dict.__delitem__("a")
    except TypeError as te:
        # --- Then
        assert te is not None
        assert te.args[0] == "'AdaendraImmutableDict' object doesn't support item deletion"


if __name__ == '__main__':
    unittest.main()
