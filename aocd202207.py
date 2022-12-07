#!/usr/bin/env python
import string

from solution import Solution

if __name__ == "__main__":
    import sys


class SessionParser:
    # session = [ lines ]
    # line = command | output
    # command = "$" "cd" dirarg| "ls"
    # dirarg = [a-z]+ | ".."
    # output = "dir" ident | int filename
    # ident = [a-z]+
    # int = \d+
    # filename = [a-z.]+

    def cdn(self):
        return "/".join(self.dirs)

    def __init__(self):
        self.total = None
        self.dirs = []
        self.lowest_candidate = None
        self.sizes = {}

    def leave_dir(self):
        this_size = self.sizes[self.cdn()]
        self.dirs.pop()
        key = self.cdn()
        if key in self.sizes:
            self.sizes[self.cdn()] += this_size

    def session(self, in_data):
        for line in in_data:
            if line[:2] == "$ ":
                self.command(line)
            elif line[0] in string.digits or line[:4] == "dir ":
                self.output(line)
            else:
                raise ValueError(fr"Expected '$ ' or \d+ or 'dir ' but got: {line[:4]}")
        while self.dirs:
            self.leave_dir()
        self.total = 0
        unused = 70_000_000 - self.sizes["/"]
        require = 30_000_000 - unused
        self.lowest_candidate = require + 100_000_000
        for k, v in self.sizes.items():
            if v <= 100_000:
                self.total += v
            if require <= v < self.lowest_candidate:
                self.lowest_candidate = v

    def output(self, line):
        if line[0] in string.digits:
            size, ident = line.split()
            self.sizes[self.cdn()] += int(size)
        elif line[:4] != "dir ":
            raise ValueError(fr"Expected '$ ' or \d+ or 'dir ' but got: {line[:4]}")

    def dir_arg(self, line):
        if line == "..":
            self.leave_dir()
        else:
            self.dirs.append(line)
            self.sizes[self.cdn()] = 0

    def command(self, line):
        if line[:2] != "$ ":
            raise ValueError(f"Expected '$ ' but got {line[:2]}")
        if line[2:5] == "cd ":
            self.dir_arg(line[5:])
        elif line[2:] != "ls":
            raise ValueError(f"Expected dir or ls but got {line[:2]}")


class Aocd202207(Solution):

    @classmethod
    def doit(cls, data: [str]) -> int:
        sp = SessionParser()
        sp.session(data)
        return sp.total

    @classmethod
    def doit2(cls, data: [str]):
        sp = SessionParser()
        sp.session(data)
        return sp.lowest_candidate

    def task1(self):
        return self.doit(self.input_data)

    def task2(self):
        return self.doit2(self.input_data)


# Tests #######################################################################
test_data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".split("\n")[1:-1]  # we need to split and slice, to comply with Solution class.


def test_doit():
    assert Aocd202207.doit(test_data) == 95437


def test_doit2():
    assert Aocd202207.doit2(test_data) == 24933642


def test_doit_real1():
    s = Aocd202207()
    assert s.task1() == 1367870


def test_doit_real2():
    s = Aocd202207()
    assert s.task2() == 549173


# Main ########################################################################


def main():
    if len(sys.argv) > 1:
        Aocd202207.test()
    else:
        s = Aocd202207()
        print(f"task 1: {s.task1()}")
        print(f"task 2: {s.task2()}")


if __name__ == "__main__":
    main()
