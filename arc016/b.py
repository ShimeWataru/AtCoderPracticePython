import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(9):
            if l[i][j] == "x":
                ans += 1
            elif l[i][j] == "o" and (i == 0 or l[i - 1][j] == "x" or l[i - 1][j] == "."):
                ans += 1
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
        input = """15
.........
.x.......
.........
...x.....
.........
.......o.
.......o.
.......o.
.........
..x.....o
........o
........o
....x...o
.x......o
........o"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6
..o..x.o.
..o..x.o.
..x..o.o.
..o..o.o.
..o..x.o.
..o..x.o."""
        output = """9"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2
.........
........."""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
