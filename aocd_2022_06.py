#!/usr/bin/env python
import pytest

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd_2022_06(Solution):
    @classmethod
    def find_seq(cls, data: str, seq_len):
        i = 0
        found = False
        while i < len(data) - seq_len and not found:
            found = len({data[i + j] for j in range(seq_len)}) == seq_len
            i += 1

        return i + seq_len - 1 if found else -1

    @classmethod
    def doit(cls, data: str) -> int:
        return cls.find_seq(data, 4)

    @classmethod
    def doit2(cls, data):
        return cls.find_seq(data, 14)

    def task1(self):
        return self.doit(self.raw_input)

    def task2(self):
        return self.doit2(self.raw_input)


# Tests #######################################################################

test_data = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
""".split("\n")[1:-1]  # we need to split and slice, to comply with Solution class.

test_list = zip(test_data, [7, 5, 6, 10, 11])

test_data2 = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
)


@pytest.mark.parametrize("test_input, expected", test_list)
def test_doit(test_input, expected):
    assert Aocd_2022_06.doit(test_input) == expected


def test_doit_real1():
    s = Aocd_2022_06()
    assert s.task1() == 1833


def test_doit_real2():
    s = Aocd_2022_06()
    assert s.task2() == 3425


@pytest.mark.parametrize("test_input, expected", test_data2)
def test_doit2(test_input, expected):
    assert Aocd_2022_06.doit2(test_input) == expected


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
