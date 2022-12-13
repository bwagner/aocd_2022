#!/usr/bin/env python
import math
from functools import cmp_to_key
from typing import Callable

import pytest
from aocd.exceptions import PuzzleLockedError

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202213(Solution):

    @classmethod
    def cmp(cls, x: int, y: int) -> int:
        return (x - y > 0) - (x - y < 0)

    @classmethod
    def cmp_len(cls, x: [], y: []) -> int:
        return cls.cmp(len(x), len(y))

    @classmethod
    def make_pairs(cls, data: str) -> [[], []]:
        return [[eval(y) for y in x.split()] for x in data.split("\n\n")]

    @classmethod
    def make_list(cls, data: str):
        result = []
        for p in cls.make_pairs(data):
            result.extend(p)
        return result

    @classmethod
    def cmp_packets(cls, left: [], right: []) -> int:
        """
        Returns -1 if left < right, 0 if left == right, 1 if left > right
        :param left:
        :param right:
        :return:
        """
        # left = packet
        # right = packet
        # packet = list
        # list = empty_list | [item]
        # item = int | list
        for i, j in zip(left, right):
            if all(type(x) == int for x in (i, j)):
                if (r := cls.cmp(i, j)) != 0:
                    return r
                continue
            if all(type(x) == list for x in (i, j)):
                for f in (cls.cmp_packets, cls.cmp_len):
                    f: Callable[[[], []], int]
                    if (r := f(i, j)) != 0:
                        return r
                continue
            return (
                cls.cmp_packets(i, [j]) if type(i) == list else cls.cmp_packets([i], j)
            )
        return cls.cmp_len(left, right)

    @classmethod
    def doit1(cls, data: str) -> int:
        pairs = cls.make_pairs(data)
        return sum(
            ci
            for ci, (left, right) in enumerate(pairs, start=1)
            if cls.cmp_packets(left, right) == -1
        )

    @classmethod
    def doit2(cls, data: str) -> int:
        pl = Aocd202213.make_list(data) + [[[x]] for x in (2, 6)]
        pls = sorted(pl, key=cmp_to_key(Aocd202213.cmp_packets))
        return math.prod(pls.index([[x]]) + 1 for x in (2, 6))

    def task1(self):
        return self.doit1(self.raw_data)

    def task2(self):
        return self.doit2(self.raw_data)


test_cmp_len_data = (
    (([1, 1, 1], [1, 1, 1, 1, 1]), -1),
    (([1, 1, 1, 1, 1], [1, 1, 1]), 1),
    (([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 0),
)


@pytest.mark.parametrize("inp, exp", test_cmp_len_data)
def test_cmp_len(inp, exp):
    assert Aocd202213.cmp_len(*inp) == exp


# Tests
test_data = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip()

test_cmp = (
    (([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]), -1),
    (([9], [[8, 7, 6]]), 1),
    (([[4, 4], 4, 4], [[4, 4], 4, 4, 4]), -1),
    (([7, 7, 7, 7], [7, 7, 7]), 1),
    (([], [3]), -1),
    (([[[]]], [[]]), 1),
    (([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]), 1),
)


@pytest.mark.parametrize("inp, exp", test_cmp)
def test_cmp_1(inp, exp):
    assert Aocd202213.cmp_packets(*inp) == exp


def test_doit():
    assert Aocd202213.doit1(test_data) == 13


def test_doit2():
    assert Aocd202213.doit2(test_data) == 140


def test_doit_real1():
    s = Aocd202213()
    assert s.task1() == 6101


def test_make_list():
    assert Aocd202213.make_list(test_data) == [
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
        [[1], [2, 3, 4]],
        [[1], 4],
        [9],
        [[8, 7, 6]],
        [[4, 4], 4, 4],
        [[4, 4], 4, 4, 4],
        [7, 7, 7, 7],
        [7, 7, 7],
        [],
        [3],
        [[[]]],
        [[]],
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
    ]


def test_doit_real2():
    s = Aocd202213()
    assert s.task2() == 21909


# Main


def main():
    if len(sys.argv) > 1:
        Aocd202213.test()
    else:
        try:
            s = Aocd202213()
        except PuzzleLockedError as e:
            print(f"Hold your horses! {e}")
        else:
            print(f"task 1: {s.task1()}")
            print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
