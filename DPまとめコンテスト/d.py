import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    N, W = map(int, input().split())
    w = [0] * N
    v = [0] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split())
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j - w[i] >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[i]] + v[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[N][W])


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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
