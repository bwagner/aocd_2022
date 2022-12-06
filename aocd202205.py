#!/usr/bin/env python
import re

from solution import Solution

if __name__ == "__main__":
    import sys


class Aocd202205(Solution):

    @classmethod
    def transpose(cls, stacks: [str]) -> [str]:
        """
        Cleans out clutter and transposes into list where s[i, j] becomes s[j, i]
        :param stacks: The list of stacks top to bottom
        :return: The list of stacks left to right, uncluttered, i.e. [] removed
        """
        new_stack = [[" "] * len(stacks) for _ in range((len(stacks[0]) + 1) // 4)]
        for r, row in enumerate(stacks):
            for c, col in enumerate(x for i, x in enumerate(row) if i % 4 == 1):
                new_stack[c][r] = col
        return new_stack

    @classmethod
    def get_stacks_and_moves(cls, lines: [str]) -> ([str], [str]):
        stacks = []
        i = 0
        while line := lines[i]:
            stacks.append(line)
            i += 1
        moves = lines[i + 1:]

        return stacks, moves

    @classmethod
    def perform_moves(cls, stacks: [[str]], moves: [str]):
        c_stacks = [[y for y in reversed(r) if y != " "] for r in stacks]
        for move in moves:
            count, src, dst = [int(x) - 1 for x in re.findall(r"\d+", move)]
            count += 1
            for _ in range(count):
                c_stacks[dst].append(c_stacks[src].pop())
        return "".join([s.pop() for s in c_stacks])

    @classmethod
    def perform_moves2(cls, stacks: [[str]], moves: [str]):
        c_stacks = [[y for y in reversed(r) if y != " "] for r in stacks]
        for move in moves:
            count, src, dst = [int(x) - 1 for x in re.findall(r"\d+", move)]
            count += 1
            c_stacks[dst] += c_stacks[src][-count:]
            c_stacks[src] = c_stacks[src][:-count]
        return "".join([s.pop() for s in c_stacks])

    @classmethod
    def get_top_crates(cls, all_lines: [str]) -> str:
        (stacks, moves) = cls.get_stacks_and_moves(all_lines)
        return cls.perform_moves(cls.transpose(stacks), moves)

    @classmethod
    def get_task1(cls, all_lines: [str]) -> str:
        return cls.get_top_crates(all_lines)

    @classmethod
    def get_top_crates2(cls, all_lines: [str]) -> str:
        (stacks, moves) = cls.get_stacks_and_moves(all_lines)
        return cls.perform_moves2(cls.transpose(stacks), moves)

    @classmethod
    def get_task2(cls, all_lines: [str]) -> str:
        return cls.get_top_crates2(all_lines)

    def task1(self):
        return self.get_task1(self.input_data)

    def task2(self):
        return self.get_task2(self.input_data)


# Tests #######################################################################

test_data = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".split("\n")[1:-1]


# we need to split and slice, since that's what the Solution class provides us.

def test_get_sm_1():
    stacks = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]

    moves = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    assert Aocd202205.get_stacks_and_moves(test_data) == (stacks, moves)


def test_transpose():
    stacks = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]
    stacks_t = [
        [" ", "N", "Z", "1"],
        ["D", "C", "M", "2"],
        [" ", " ", "P", "3"],
    ]
    assert Aocd202205.transpose(stacks) == stacks_t


def test_crates1():
    stacks = [
        [" ", "N", "Z", "1"],
        ["D", "C", "M", "2"],
        [" ", " ", "P", "3"],
    ]
    moves = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    assert Aocd202205.perform_moves(stacks, moves) == "CMZ"


def test_crates2():
    stacks = [
        [" ", "N", "Z", "1"],
        ["D", "C", "M", "2"],
        [" ", " ", "P", "3"],
    ]
    moves = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    assert Aocd202205.perform_moves2(stacks, moves) == "MCD"


def test_get_top_crates():
    assert Aocd202205.get_top_crates(test_data) == "CMZ"


def test_get_top_crates2():
    assert Aocd202205.get_top_crates2(test_data) == "MCD"


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd202205.test()
    else:
        s = Aocd202205()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
