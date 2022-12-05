#!/usr/bin/env python
import pytest

from solution import Solution

if __name__ == "__main__":
    import sys

rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6


class Aocd_2022_02(Solution):
    a = x = rock
    b = y = paper
    c = z = scissors

    map_moves = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    map_score = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    """
         my_move
         r   p   s
         1   2   3
    r 1  0d  1w  2l
    p 2 -1l  0d  1w
    s 3 -2w -1l  0d

    """

    @classmethod
    def eval_game(cls, ops_move: int, my_move: int) -> int:
        if ops_move == my_move:
            # takes care of 1,1 2,2 3,3
            score = draw
        else:
            score = win if my_move - ops_move in (1, -2) else lose
        return my_move + score

    @classmethod
    def get_score(cls, data: [str]) -> int:
        total = 0
        for game in data:
            ops_move, my_move = game.split()
            total += cls.eval_game(
                cls.map_score[ops_move], cls.map_score[cls.map_moves[my_move]]
            )
        return total

    # for 2nd half of puzzle:
    map_xyz = {
        "X": lose,
        "Y": draw,
        "Z": win,
    }

    @classmethod
    def force_outcome(cls, given_move, outcome):
        if outcome == draw:
            return given_move
        if outcome == win:
            # 1 -> 2
            # 2 -> 3
            # 3 -> 1
            return given_move % 3 + 1
        # 1 -> 3
        # 2 -> 1
        # 3 -> 2
        return (given_move + 1) % 3 + 1

    @classmethod
    def get_score2(cls, data: [str]) -> int:
        total = 0
        for game in data:
            ops_move, outcome = game.split()
            total += cls.eval_game(
                cls.map_score[ops_move],
                cls.force_outcome(cls.map_score[ops_move], cls.map_xyz[outcome]),
            )
        return total

    def task1(self):
        return self.get_score(self.input_data)

    def task2(self):
        return self.get_score2(self.input_data)


# Tests #######################################################################

test_data = """
A Y
B X
C Z
""".split("\n")[1:-1]
# we need to split and slice, since that's what the Solution class provides us.


def test_get_score():
    assert Aocd_2022_02.get_score(test_data) == 15


def test_real_1():
    s = Aocd_2022_02()
    assert s.task1() == 13565


test_data_force = (
    ((rock, win), paper),
    ((paper, win), scissors),
    ((scissors, win), rock),
    ((rock, draw), rock),
    ((paper, draw), paper),
    ((scissors, draw), scissors),
    ((rock, lose), scissors),
    ((paper, lose), rock),
    ((scissors, lose), paper),
)


@pytest.mark.parametrize("test_input, expected", test_data_force)
def test_force_win_rock(test_input, expected):
    assert Aocd_2022_02.force_outcome(*test_input) == expected


def test_get_score2():
    assert Aocd_2022_02.get_score2(test_data) == 12


def test_real_2():
    s = Aocd_2022_02()
    assert s.task2() == 12424


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd_2022_02.test()
    else:
        s = Aocd_2022_02()
        print(f"task 1: {s.task1()}")
        print(f"task 1: {s.task1()}")


if __name__ == "__main__":
    main()
