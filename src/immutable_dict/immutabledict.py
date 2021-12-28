from copy import deepcopy


def immutable(self, *args, **kwargs):
    r"""
    Function for not implemented method since the object is immutable.
    :param self: The immutable object which has an update function called.
    """
    raise AttributeError(f"'{self.__class__.__name__}' object is read-only")


class ImmutableDict(dict):
    r"""
    Class to create an immutable dictionary.

    It works as same as `dict`, without methods that can change the
    immutability. In addition, it supports __hash__().
    
    :param dict: dict - The dictionary to set as immutable.
    """

    # Little tric to save RAM -> https://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = (
        "_hash",
    )

    # Decorator to let know that this method is available for the static object and all its instances.
    @classmethod
    def fromkeys(cls, *args, **kwargs):
        r"""
        Use the method dict.fromkeys and take the result to generate the Immutable Dict.
        """
        print(cls)
        return cls(dict.fromkeys(*args, **kwargs))

    def __init__(self, *args, **kwargs):
        pass

    def __hash__(self, *args, **kwargs):
        r"""
        Calculates the hash if all values are hashable, otherwise raises a 
        TypeError.
        """
        print("ImmutableDict.hash")

        if self._hash != None:
            _hash = self._hash
        else:
            try:
                fs = frozenset(self.items())
            except TypeError:
                _hash = -1
            else:
                _hash = hash(fs)

            object.__setattr__(self, "_hash", _hash)

        if _hash == -1:
            raise TypeError("Not all values are hashable.")

        return _hash

    def __repr__(self, *args, **kwargs):
        r"""
        Identical to dict.__repr__().
        Represent the class object as a String.

        Format : <Class Name>(<Body>)
        """
        print("ImmutableDict.repr")

        class_name = self.__class__.__name__
        body = super().__repr__(*args, **kwargs)

        return f"{class_name}({body})"

    def copy(self):
        print("ImmutableDict.copy")
        r"""
        Return the object itself, as it's an immutable.
        """

        return self

    def __copy__(self, *args, **kwargs):
        r"""
        See copy().
        """

        return self.copy()

    def __deepcopy__(self, *args, **kwargs):
        r"""
        As for tuples, if hashable, see copy(); otherwise, it returns a 
        deepcopy.
        """

        try:
            hash(self)
        except TypeError:
            tmp = deepcopy(dict(self))

            return self.__class__(tmp)

        return self.__copy__(*args, **kwargs)

    def __reduce__(self, *args, **kwargs):
        r"""
        Support for `pickle`.
        """

        return self.__class__, (dict(self),)

    def __setitem__(self, key, val, *args, **kwargs):
        raise TypeError(
            f"'{self.__class__.__name__}' object doesn't support item "
            "assignment"
        )

    def __delitem__(self, key, *args, **kwargs):
        raise TypeError(
            f"'{self.__class__.__name__}' object doesn't support item "
            "deletion"
        )


def immutabledict_or(self, other, *args, **kwargs):
    print("immutabledict_or")
    return self


ImmutableDict.___or__ = immutabledict_or
ImmutableDict.__ior__ = immutabledict_or  # In place operator : https://docs.python.org/3/library/operator.html#in-place-operators

ImmutableDict.clear = immutable
ImmutableDict.pop = immutable
ImmutableDict.popitem = immutable
ImmutableDict.setdefault = immutable
ImmutableDict.update = immutable
ImmutableDict.__delattr__ = immutable
ImmutableDict.__setattr__ = immutable


def frozen_new(e4b37cdf_d78a_4632_bade_6f0579d8efac, *args, **kwargs):
    print("frozen_new")
    print(e4b37cdf_d78a_4632_bade_6f0579d8efac)
    cls = e4b37cdf_d78a_4632_bade_6f0579d8efac

    has_kwargs = bool(kwargs)
    continue_creation = True

    # check if there's only an argument and it's of the same class
    if len(args) == 1 and not has_kwargs:
        it = args[0]

        # no isinstance, to avoid subclassing problems
        if (
                (it.__class__ == ImmutableDict and cls == ImmutableDict)
        ):
            self = it
            continue_creation = False

    if continue_creation:
        self = dict.__new__(cls, *args, **kwargs)

        dict.__init__(self, *args, **kwargs)

        # empty singleton - start

        if self.__class__ == ImmutableDict and not len(self):
            try:
                self = cls.empty
                continue_creation = False
            except AttributeError:
                cls.empty = self

        # empty singleton - end

        if continue_creation:
            object.__setattr__(self, "_hash", None)

    return self


ImmutableDict.__new__ = frozen_new

__all__ = (ImmutableDict.__name__,)
