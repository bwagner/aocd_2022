#!/usr/bin/env python

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd_2022_01(Solution):

    @classmethod
    def collect(cls, data: [str]) -> list[int]:
        amounts = []
        current_sum = 0
        for line in data:
            if line:
                current_sum += int(line)
            else:
                amounts.append(current_sum)
                current_sum = 0
        amounts.append(current_sum)

        return amounts

    @classmethod
    def find_max(cls, data: str) -> int:
        return max(cls.collect(data))

    @classmethod
    def find_max3(cls, data: str) -> int:
        return sum(sorted(cls.collect(data))[-3:])

    def task1(self):
        return self.find_max(self.input_data)

    def task2(self):
        return self.find_max3(self.input_data)


# Tests #######################################################################

test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
    """.strip().split("\n")
# we need to strip and split, since that's what the Solution class provides us.


def test_find_max():
    assert Aocd_2022_01.find_max(test_data) == 24_000


def test_find_max3():
    assert Aocd_2022_01.find_max3(test_data) == 45_000


def test_real_1():
    s = Aocd_2022_01()
    assert s.task1() == 69626


def test_real_2():
    s = Aocd_2022_01()
    assert s.task2() == 206780


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd_2022_01.test()
    else:
        s = Aocd_2022_01()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
