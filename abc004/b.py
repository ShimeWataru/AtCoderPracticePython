import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = [list(input().split()) for i in range(4)]
    for i in range(4):
        ll = ""
        for j in range(4):
            ll += l[-i - 1][-j - 1]
            if not (j == 3):
                ll += " "
        print(ll)


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
        input = """. . . .
. o o .
. x x .
. . . ."""
        output = """. . . .
. x x .
. o o .
. . . ."""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """o o x x
o o x x
x x o o
x x o o"""
        output = """o o x x
o o x x
x x o o
x x o o"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
