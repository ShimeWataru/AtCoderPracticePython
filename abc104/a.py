import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    if n < 1200:
        print("ABC")
    elif n < 2800:
        print("ARC")
    else:
        print("AGC")


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
        input = """1199"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1200"""
        output = """ARC"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4208"""
        output = """AGC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
