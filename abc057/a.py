import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    print((a+b) % 24)


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
        input = """9 12"""
        output = """21"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """19 0"""
        output = """19"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """23 2"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
