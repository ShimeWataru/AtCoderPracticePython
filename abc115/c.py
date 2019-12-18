import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = [int(input()) for i in range(n)]
    l = sorted(l)
    min_l = 99999999999
    for i in range(n - k + 1):
        min_l = min(min_l, l[i + k - 1] - l[i])
    print(min_l)


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
10
15
11
14
12"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 3
5
7
5
7
7"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
