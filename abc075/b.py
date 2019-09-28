import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def count_mine(m, i, j):
    count = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if m[k][l] == "#":
                count += 1
    return count


def resolve():
    H, W = map(int, input().split())
    l = [list(map(str, input().split())) for i in range(H)]
    m = []
    m.append("*" * (W + 2))
    for i in range(len(l)):
        add_colum = "*" + ''.join(l[i]) + "*"
        m.append(add_colum)
    m.append("*" * (W + 2))
    answer = []
    for i in range(1, H + 1):
        answer_column = ""
        for j in range(1, W + 1):
            if m[i][j] == ".":
                answer_column += str(count_mine(m, i, j))
            else:
                answer_column += "#"
        answer.append(answer_column)

    for i in range(H):
        print(answer[i])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        print("test_input_1")
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
