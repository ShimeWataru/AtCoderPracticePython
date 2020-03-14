import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = [0]*n
    b = [0]*n
    c = [0]*n
    for i in range(n):
        a[i], b[i], c[i] = map(int, input().split())
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = [a[0], b[0], c[0]]
    for i in range(n - 1):
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][1] +
                           a[i+1], dp[i][2] + a[i + 1])
        dp[i + 1][1] = max(dp[i + 1][0], dp[i][0] +
                           b[i+1], dp[i][2] + b[i + 1])
        dp[i + 1][2] = max(dp[i + 1][0], dp[i][0] +
                           c[i + 1], dp[i][1] + c[i + 1])
    print(max(dp[n-1]))


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
        input = """3
10 40 70
20 50 80
30 60 90"""
        output = """210"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1
100 10 1"""
        output = """100"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1"""
        output = """46"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
