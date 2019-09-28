import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def check(m, i, j, H, W):
    left = False
    up = False
    right = False
    down = False
    left = ((j == 0) or (m[i][j-1] == "#"))
    up = ((i == 0) or (m[i-1][j] == "#"))
    right = ((j == (W - 1)) or (m[i][j+1] == "#"))
    down = ((i == (H-1)) or (m[i+1][j] == "#"))
    return left or right or up or down


def resolve():
    H, W = map(int, input().split())
    l = [str(input()) for i in range(H)]
    ans = "Yes"
    for i in range(H):
        for j in range(W):
            if (l[i][j] == "#") and (not(check(l, i, j, H, W))):
                ans = "No"
    print(ans)


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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
