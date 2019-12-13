import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
        print("Possible")
    else:
        print("Impossible")


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
        input = """4 5"""
        output = """Possible"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1 1"""
        output = """Impossible"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
