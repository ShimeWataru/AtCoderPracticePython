import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, k = map(int, input().split())
    change_a = max(0, a - k)
    if a < k:
        b = max(0, b - (k - a))
    print(change_a, b)


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
        input = """2 3 3"""
        output = """0 2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """500000000000 500000000000 1000000000000"""
        output = """0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
