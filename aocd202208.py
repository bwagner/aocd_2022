#!/usr/bin/env python
import math

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202208(Solution):
    # We're dealing with single digit values, so
    # a conversion to int is not necessary for correctness.
    # For performance, it *would be* necessary, though.
    @classmethod
    def count_visible_trees(cls, data: [str]) -> int:
        visible_trees = 0
        skip = 1  # skip rim
        for r, row in enumerate(data[skip:-skip]):
            r_ = r + skip  # adjust for the offset
            for c, col in enumerate(row[skip:-skip]):
                c_ = c + skip  # adjust for the offset
                visible_left = all(kol < col for kol in data[r_][:c_])
                visible_right = all(kol < col for kol in data[r_][c_ + 1 :])
                visible_up = all(sow[c_] < col for sow in data[:r_])
                visible_down = all(sow[c_] < col for sow in data[r_ + 1 :])
                visible_trees += any(
                    [visible_left, visible_right, visible_up, visible_down]
                )
        return visible_trees + 2 * (len(data) + len(data[0]) - 2)

    @classmethod
    def get_max_score(cls, data: [str]) -> int:
        max_score = 0
        skip = 1  # skip rim
        for r in range(skip, len(data) - skip):
            row = data[r]
            for c in range(skip, len(row) - skip):
                col = row[c]
                # algorithm:
                # from the tree's position iterate outwards, i.e.
                # center to left (score_left), center to right (score_right)
                # center to top (score_up), center to bottom (score_down)

                score_left = 0
                for i in range(c - 1, -1, -1):
                    score_left += 1
                    if row[i] >= col:
                        break

                score_right = 0
                for i in range(c + 1, len(row)):
                    score_right += 1
                    if row[i] >= col:
                        break

                score_up = 0
                for i in range(r - 1, -1, -1):
                    score_up += 1
                    if data[i][c] >= col:
                        break

                score_down = 0
                for i in range(r + 1, len(data)):
                    score_down += 1
                    if data[i][c] >= col:
                        break

                if (
                    score := math.prod([score_left, score_right, score_up, score_down])
                ) > max_score:
                    max_score = score
        return max_score

    def task1(self):
        return self.count_visible_trees(self.input_data)

    def task2(self):
        return self.get_max_score(self.input_data)


# Tests #######################################################################
test_data = """
30373
25512
65332
33549
35390
""".split(
    "\n"
)[
    1:-1
]  # we need to split and slice, to comply with Solution class.


def test_doit():
    assert Aocd202208.count_visible_trees(test_data) == 21


def test_doit2():
    assert Aocd202208.get_max_score(test_data) == 8


def test_doit_real1():
    s = Aocd202208()
    assert s.task1() == 1705


def test_doit_real2():
    s = Aocd202208()
    assert s.task2() == 371200


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
