#!/usr/bin/env python

import pytest
from aocd.exceptions import PuzzleLockedError

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202209(Solution):
    @classmethod
    def doit1(cls, data: [str]) -> int:
        return 1

    @classmethod
    def doit2(cls, data: [str]) -> int:
        return 2

    def task1(self):
        return self.doit1(self.input_data)

    def task2(self):
        return self.doit2(self.input_data)


# Tests #######################################################################
test_data = """
""".split(
    "\n"
)[
    1:-1
]  # we need to split and slice, to comply with Solution class.


def test_doit():
    assert Aocd202209.doit1(test_data) == 1


def test_doit2():
    assert Aocd202209.doit2(test_data) == 2


def test_doit_real1():
    with pytest.raises(PuzzleLockedError):
        s = Aocd202209()
        assert s.task1() == 1


def test_doit_real2():
    with pytest.raises(PuzzleLockedError):
        s = Aocd202209()
        assert s.task2() == 2


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd202209.test()
    else:
        try:
            s = Aocd202209()
        except PuzzleLockedError as e:
            print(f"Hold your horses! {e}")
        else:
            print(f"task 1: {s.task1()}")
            print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
