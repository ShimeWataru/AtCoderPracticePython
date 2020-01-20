import functools
import fractions
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    lcm_l = lcm_list(l)
    for i in range(n):
        ans += (lcm_l // l[i])
    print(ans % (10 ** 9 + 7))


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
2 3 4"""
        output = """13"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
12 12 12 12 12"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3
1000000 999999 999998"""
        output = """996989508"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
