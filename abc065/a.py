import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    x, a, b = map(int, input().split())
    if b - a <= 0:
        print("delicious")
    elif b - a <= x:
        print("safe")
    else:
        print("dangerous")


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
        input = """4 3 6"""
        output = """safe"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6 5 1"""
        output = """delicious"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3 7 12"""
        output = """dangerous"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
