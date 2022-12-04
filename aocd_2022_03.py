#!/usr/bin/env python
from solution import Solution

if __name__ == "__main__":
    import sys

from string import ascii_lowercase as al


class Aocd_2022_03(Solution):

    @classmethod
    def get_priority(cls, char: str) -> int:
        return ord(char) + 1 - [ord("A") - len(al), ord("a")][char.islower()]

    @classmethod
    def get_lines(cls, data_str: str) -> list[str]:
        return [x for x in data_str.split() if x]

    @classmethod
    def get_sum(cls, data: [str]) -> int:
        total = 0
        for d in data:
            middle = len(d) // 2
            common = set(d[:middle]) & set(d[middle:])
            total += sum(Aocd_2022_03.get_priority(x) for x in common)
        return total

    @classmethod
    def get_sum2(cls, data: [str]) -> int:
        total = 0
        group_size = 3
        for i in range(0, len(data), group_size):
            sets = [set(x) for x in data[i: i + group_size]]
            intersection = set.intersection(*sets)
            badge = intersection.pop()
            total += Aocd_2022_03.get_priority(badge)
        return total

    def task1(self):
        return self.get_sum(self.input_data)

    def task2(self):
        return self.get_sum2(self.input_data)


# Tests #######################################################################

test_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip().split()
# we need to strip and split, since that's what the Solution class provides us.


def test_sum_1():
    assert Aocd_2022_03.get_sum(test_data) == 157


def test_priority_a():
    assert Aocd_2022_03.get_priority("a") == 1


def test_priority_z():
    assert Aocd_2022_03.get_priority("z") == 26


def test_priority_A():
    assert Aocd_2022_03.get_priority("A") == 27


def test_priority_Z():
    assert Aocd_2022_03.get_priority("Z") == 52


def test_real_1():
    s = Aocd_2022_03()
    assert s.task1() == 8039


# Part 2:
def test_prio2():
    assert Aocd_2022_03.get_sum2(test_data) == 70


def test_real_2():
    s = Aocd_2022_03()
    assert s.task2() == 2510


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd_2022_03.test()
    else:
        s = Aocd_2022_03()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
