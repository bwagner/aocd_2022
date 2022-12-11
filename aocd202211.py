#!/usr/bin/env python
import math
import re

import pytest
from aocd.exceptions import PuzzleLockedError

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202211(Solution):
    @classmethod
    def doit1(cls, data: [str]) -> int:
        return cls.get_monkey_business(data, 20)

    @classmethod
    def doit2(cls, data: [str]) -> int:
        return cls.get_monkey_business(data, 10_000, part1=False)

    def task1(self):
        return self.doit1(self.input_data)

    def task2(self):
        return self.doit2(self.input_data)

    @classmethod
    def read_monkeys(cls, data):
        monkeys = cls.read_monkeys_raw(data)
        for monkey in monkeys:
            monkey[1] = eval(f"lambda old: {monkey[1]}")
        return monkeys

    @classmethod
    def read_monkeys_raw(cls, data):
        dc = data.copy()
        monkeys = []
        while dc:
            dc.pop(0)  # skip Monkey number
            si = [int(x) for x in re.findall(r"\d+", dc.pop(0))]
            op = re.search(r"Operation: new = (.*)", dc.pop(0)).groups()[0]
            db = int(re.search(r"Test: divisible by (\d+)", dc.pop(0)).groups()[0])
            t = int(re.search(r"If true: throw to monkey (\d+)", dc.pop(0)).groups()[0])
            f = int(re.search(r"If false: throw to monkey (\d+)", dc.pop(0)).groups()[0])
            monkeys.append([
                si, op, db, [t, f], 0  # number of inspected items
            ])
            if dc:
                dc.pop(0)  # skip empty line

        return monkeys

    @classmethod
    def process_monkeys(cls, monkeys, part1=True):
        # find common divisor that will reduce the numbers
        # but keeps the relation between the "divides by" numbers
        cd = math.lcm(*[m[2] for m in monkeys])
        for monkey in monkeys:
            op = monkey[1]
            db = monkey[2]
            t, f = monkey[3]
            while monkey[0]:
                monkey[4] += 1
                wl = op(monkey[0].pop(0))
                wl = (int(wl / 3) if part1 else wl) % cd
                target = [f, t][wl % db == 0]
                monkeys[target][0].append(wl)

    @classmethod
    def get_monkey_business(cls, monkeys_raw, rounds, part1=True):
        monkeys = cls.read_monkeys(monkeys_raw)
        for _ in range(rounds):
            cls.process_monkeys(monkeys, part1)
        return math.prod([x[4] for x in sorted(monkeys, key=lambda x: x[4])[-2:]])


# Tests
test_data = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".split(
    "\n"
)[
            1:-1
            ]  # we need to split and slice, to comply with Solution class.


def test_read_monkeys_raw(check):
    monkeys = Aocd202211.read_monkeys_raw(test_data)
    with check:
        assert len(monkeys) == 4
    assert monkeys == [
        [
            [79, 98],
            "old * 19",
            23,
            [2, 3],
            0,
        ],
        [
            [54, 65, 75, 74],
            "old + 6",
            19,
            [2, 0],
            0,
        ],
        [
            [79, 60, 97],
            "old * old",
            13,
            [1, 3],
            0,
        ],
        [
            [74],
            "old + 3",
            17,
            [0, 1],
            0,
        ],
    ]


def test_pm_1(check):
    monkeys = Aocd202211.read_monkeys(test_data)
    Aocd202211.process_monkeys(monkeys)
    with check:
        assert monkeys[0][0] == [20, 23, 27, 26]
    with check:
        assert monkeys[1][0] == [2080, 25, 167, 207, 401, 1046]
    with check:
        assert monkeys[2][0] == []
    with check:
        assert monkeys[3][0] == []
    Aocd202211.process_monkeys(monkeys)
    with check:
        assert monkeys[0][0] == [695, 10, 71, 135, 350]
    with check:
        assert monkeys[1][0] == [43, 49, 58, 55, 362]
    with check:
        assert monkeys[2][0] == []
    with check:
        assert monkeys[3][0] == []
    Aocd202211.process_monkeys(monkeys)
    with check:
        assert monkeys[0][0] == [16, 18, 21, 20, 122]
    with check:
        assert monkeys[1][0] == [1468, 22, 150, 286, 739]
    with check:
        assert monkeys[2][0] == []
    with check:
        assert monkeys[3][0] == []


def test_count(check):
    monkeys = Aocd202211.read_monkeys(test_data)
    for _ in range(20):
        Aocd202211.process_monkeys(monkeys)
    with check:
        assert monkeys[0][4] == 101
    with check:
        assert monkeys[1][4] == 95
    with check:
        assert monkeys[2][4] == 7
    with check:
        assert monkeys[3][4] == 105


test_d2 = (
    (1, (2, 4, 3, 6)),
    (20, (99, 97, 8, 103)),
    (1000, (5204, 4792, 199, 5192)),
    (2000, (10419, 9577, 392, 10391)),
    (10000, (52166, 47830, 1938, 52013)),
)


@pytest.mark.parametrize("inp, exp", test_d2)
def test_count2(check, inp, exp):
    monkeys = Aocd202211.read_monkeys(test_data)
    for _ in range(inp):
        Aocd202211.process_monkeys(monkeys, part1=False)
    with check:
        assert monkeys[0][4] == exp[0]
    with check:
        assert monkeys[1][4] == exp[1]
    with check:
        assert monkeys[2][4] == exp[2]
    with check:
        assert monkeys[3][4] == exp[3]


def test_monkey_business():
    assert Aocd202211.get_monkey_business(test_data, 20) == 10605


def test_doit():
    assert Aocd202211.doit1(test_data) == 10605


def test_doit2():
    assert Aocd202211.doit2(test_data) == 2713310158


def test_doit_real1():
    s = Aocd202211()
    assert s.task1() == 119715


def test_doit_real2():
    s = Aocd202211()
    assert s.task2() == 18085004878


# Main


def main():
    if len(sys.argv) > 1:
        Aocd202211.test()
    else:
        try:
            s = Aocd202211()
        except PuzzleLockedError as e:
            print(f"Hold your horses! {e}")
        else:
            print(f"task 1: {s.task1()}")
            print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
