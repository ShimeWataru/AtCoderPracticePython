import copy
import fractions
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    front = [0] * len(l)
    back = [0] * len(l)
    front[0] = l[0]
    back[0] = l[-1]
    if len(l) == 2:
        ans = max(l[0], l[1])
    else:
        for i in range(len(l) - 1):
            front[i + 1] = fractions.gcd(front[i], l[i+1])
            back[i + 1] = fractions.gcd(back[i], l[-i - 2])
        for i in range(len(l)):
            if i == 0:
                ans_i = back[-len(l) + 1]
            elif i == len(l) - 1:
                ans_i = front[len(l) - 1]
            else:
                ans_i = fractions.gcd(front[i - 1], back[len(l) - (i + 2)])
            if ans < ans_i:
                ans = ans_i
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
        input = """4
7 6 8 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
