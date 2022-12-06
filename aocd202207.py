#!/usr/bin/env python
import pytest
from aocd.exceptions import PuzzleLockedError

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202207(Solution):

    @classmethod
    def doit(cls, data: str) -> int:
        return 5

    @classmethod
    def doit2(cls, data):
        return 5

    def task1(self):
        return self.doit(self.input_data[0])

    def task2(self):
        return self.doit2(self.input_data[0])


# Tests #######################################################################

test_data = """
7
5
6
10
11
""".split("\n")[1:-1]  # we need to split and slice, to comply with Solution class.

test_list = zip(test_data, [5, 5, 5, 5, 5])


@pytest.mark.parametrize("test_input, expected", test_list)
def test_doit(test_input, expected):
    assert Aocd202207.doit(test_input) == expected


def test_doit_real1():
    with pytest.raises(PuzzleLockedError):
        s = Aocd202207()


def test_doit_real2():
    with pytest.raises(PuzzleLockedError):
        s = Aocd202207()


@pytest.mark.parametrize("test_input, expected", test_list)
def test_doit2(test_input, expected):
    assert Aocd202207.doit2(test_input) == expected


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd202207.test()
    else:
        s = Aocd202207()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
