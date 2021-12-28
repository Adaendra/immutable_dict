import unittest

from src.immutable_dict.immutabledict import ImmutableDict

def test_something():
    fd = ImmutableDict({"Sulla": "Marco", "Hicks": "Bill"})
    fd2 = ImmutableDict({"a": "1", "b": "2"})

    print("---------------")
    print(fd)
    # frozendict({'Sulla': 'Marco', 'Hicks': 'Bill'})

    print("+++++++++++++++")
    print(fd["Sulla"])

    print(">>>>>>>>>>>")
    print(fd.fromkeys("Sulla"))

    print("+++++++++++++++")
    t = (fd | fd2)
    print(len(t))
    print("+++++++++++++++")
    t = fd.__ior__(fd2)
    print(len(t))


if __name__ == '__main__':
    unittest.main()
