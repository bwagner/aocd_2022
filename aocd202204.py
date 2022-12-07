#!/usr/bin/env python
import re

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202204(Solution):
    @classmethod
    def get_two_pairs(cls, pair):
        # pair = "6-6,4-6"
        nums = [int(x) for x in re.findall(r"\d+", pair)]
        assert len(nums) == 4
        left, right = set(range(nums[0], nums[1] + 1)), set(range(nums[2], nums[3] + 1))
        return left, right

    @classmethod
    def get_subset_count(cls, pairs: [str]) -> int:
        count = 0
        for pair in pairs:
            left, right = cls.get_two_pairs(pair)
            count += left & right in (left, right)

        return count

    @classmethod
    def get_overlap_count(cls, pairs: [str]) -> int:
        count = 0
        for pair in pairs:
            left, right = cls.get_two_pairs(pair)
            count += bool(left & right)

        return count

    def task1(self):
        return self.get_subset_count(self.input_data)

    def task2(self):
        return self.get_overlap_count(self.input_data)


# Tests #######################################################################

test_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".split("\n")[1:-1]
# we need to split and slice, since that's what the Solution class provides us.


def test_subset():
    assert Aocd202204.get_subset_count(test_data) == 2


def test_overlap():
    assert Aocd202204.get_overlap_count(test_data) == 4


def test_real1():
    s = Aocd202204()
    assert s.task1() == 518


def test_real2():
    s = Aocd202204()
    assert s.task2() == 909


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd202204.test()
    else:
        s = Aocd202204()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
