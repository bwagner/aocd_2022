#!/usr/bin/env python

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd_2022_05(Solution):

    @classmethod
    def get_task1(cls, all_lines: str) -> int:
        return None

    @classmethod
    def get_task2(cls, all_lines: str) -> int:
        return None

    def task1(self):
        return self.get_task1(self.input_data)

    def task2(self):
        return self.get_task1(self.input_data)


# Tests #######################################################################

test_data = """
""".strip().split()
# we need to strip and split, since that's what the Solution class provides us.


def test_subset():
    assert Aocd_2022_05.get_subset_count(test_data) == None


def test_overlap():
    assert Aocd_2022_05.get_overlap_count(test_data) == None


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd_2022_05.test()
    else:
        s = Aocd_2022_05()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
