import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)


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
        input = """30 100"""
        output = """100"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """12 100"""
        output = """50"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """0 100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
