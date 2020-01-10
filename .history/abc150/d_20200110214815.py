import math
import fractions
import functools
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm(*numbers):
    return functools.reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)


def resolve():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(n):
        l[i] = l[i] // 2
    k = l[0]
    a = lcm_list(l)
    print((m+1) // (a * 2))


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
        input = """2 50
6 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 100
14 22 40"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 1000000000
6 6 2 6 2"""
        output = """166666667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
