import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    if a + b + c <= 21:
        print("win")
    else:
        print("bust")


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
        input = """5 7 9"""
        output = """win"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """13 7 2"""
        output = """bust"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
