import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)[::-1]
    print(sum(l[:k]))


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
        input = """5 3
1 2 3 4 5"""
        output = """12"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """15 14
50 26 27 21 41 7 42 35 7 5 5 36 39 1 45"""
        output = """386"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
