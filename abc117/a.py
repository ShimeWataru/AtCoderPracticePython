import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    print(a/b)


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
        input = """8 3"""
        output = """2.6666666667"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """99 1"""
        output = """99.0000000000"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 100"""
        output = """0.0100000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
