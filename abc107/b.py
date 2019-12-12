import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    h, w = map(int, input().split())
    l = [input() for i in range(h)]
    l = [s for s in l if s.count("#") > 0]
    check = [True] * w
    for i in range(len(l[0])):
        check_row = True
        for j in range(len(l)):
            if l[j][i] == "#":
                check_row = False
        check[i] = check_row
    ans = []
    for i in range(len(l)):
        str_row = ""
        for j in range(len(l[0])):
            if not(check[j]):
                str_row += l[i][j]
        ans.append(str_row)

    for i in range(len(ans)):
        print(ans[i])


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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
