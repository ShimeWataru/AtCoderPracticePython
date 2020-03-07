import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, d = map(int, input().split())
    t = b / a
    o = d / c
    if t > o:
        print("TAKAHASHI")
    elif t < o:
        print("AOKI")
    else:
        print("DRAW")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """5 2 6 3"""
        output = """AOKI"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """100 80 100 73"""
        output = """TAKAHASHI"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """66 30 55 25"""
        output = """DRAW"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
