import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    if n == 25:
        print("Christmas")
    elif n == 24:
        print("Christmas Eve")
    elif n == 23:
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")


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
        input = """25"""
        output = """Christmas"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """22"""
        output = """Christmas Eve Eve Eve"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
