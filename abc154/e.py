import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, d = map(int, input().split())
    l = [[0 for i in range(d + 1)] for j in range(c + 1)]
    ans = 0
    for i in range(c + 1):
        for j in range(d + 1):
            if i == 0 and j == 0:
                l[i][j] = 0
            elif i == 0:
                l[i][j] = 1
            elif j == 0:
                l[i][j] = 1
            else:
                l[i][j] = l[i - 1][j] + l[i][j - 1]
                if i >= a and j >= b:
                    ans += l[i][j]
    print(ans % 1000000007)


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
        input = """1 1 2 2"""
        output = """14"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """314 159 2653 589"""
        output = """602215194"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
