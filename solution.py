#!/usr/bin/env python
import re
import sys
from abc import ABC, abstractmethod

import pytest
from aocd.models import Puzzle


class Solution(ABC):
    def __init__(self):
        year, day = get_year_day(type(self).__name__)
        self.raw_input = Puzzle(year=year, day=day).input_data
        self.input_data = self.raw_input.split("\n")

    @abstractmethod
    def task1(self):
        pass

    @abstractmethod
    def task2(self):
        pass

    def run(self):
        self.task1()
        self.task2()

    @classmethod
    def test(cls):
        pytest.main([sys.argv[0]])


def get_year_day(name):
    return tuple(
        int(x) for x in re.match(r".*(\d{4})(\d{2})", name, re.IGNORECASE).groups()
    )


def test_get_yd_1():
    assert get_year_day("aocd_202201.py") == (2022, 1)


def test_get_yd_2():
    assert get_year_day("aocd_202502.py") == (2025, 2)


def test_get_yd_3():
    assert get_year_day("Aocd_202201") == (2022, 1)


def main():
    s = Solution()
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        s.test()
    else:
        s.run()


if __name__ == "__main__":
    main()
