#!/usr/bin/env python
import string

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202208(Solution):

    @classmethod
    def doit(cls, data: [str]) -> int:
        return 5

    @classmethod
    def doit2(cls, data: [str]):
        return 5

    def task1(self):
        return self.doit(self.input_data)

    def task2(self):
        return self.doit2(self.input_data)


# Tests #######################################################################
test_data = """
""".split("\n")[1:-1]  # we need to split and slice, to comply with Solution class.


def test_doit():
    assert Aocd202208.doit(test_data) == 5


def test_doit2():
    assert Aocd202208.doit2(test_data) == 5


def test_doit_real1():
    s = Aocd202208()
    assert s.task1() == 5


def test_doit_real2():
    s = Aocd202208()
    assert s.task2() == 5


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd202208.test()
    else:
        s = Aocd202208()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
