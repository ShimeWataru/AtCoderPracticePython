import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 1000000000000
    sum_ab = sum(l)
    sum_a = [0] * n
    sum_a[0] = l[0]
    for i in range(n - 1):
        if i == 0:
            x = sum_a[0]
        else:
            x = sum_a[i - 1] + l[i]
            sum_a[i] = x
        y = sum_ab - x
        if abs(x - y) < ans:
            ans = abs(x - y)
    print(ans)


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
        input = """6
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
10 -10"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
