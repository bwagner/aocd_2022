#!/usr/bin/env python
import re

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd_2022_06(Solution):
    @classmethod
    def doit(cls, data):
        return 5

    @classmethod
    def doit2(cls, data):
        return 6

    def task1(self):
        return self.doit(self.input_data)

    def task2(self):
        return self.doit2(self.input_data)


# Tests #######################################################################

test_data = """
""".split("\n")[1:-1]  # we need to split and slice, to comply with Solution class.


def test_doit():
    assert Aocd_2022_06.doit(test_data) == 5


def test_doit2():
    assert Aocd_2022_06.doit2(test_data) == 6


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd_2022_06.test()
    else:
        s = Aocd_2022_06()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
