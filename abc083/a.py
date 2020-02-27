import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, d = map(int, input().split())
    if a + b < c + d:
        print("Right")
    elif a + b == c + d:
        print("Balanced")
    else:
        print("Left")


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
        input = """3 8 7 1"""
        output = """Left"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 4 5 2"""
        output = """Balanced"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 7 6 4"""
        output = """Right"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
