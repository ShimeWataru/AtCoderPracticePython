import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, r = map(int, input().split())
    if n > 10:
        print(r)
    else:
        print(r + 100 * (10-n))


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
        input = """2 2919"""
        output = """3719"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """22 3051"""
        output = """3051"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
