import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    ans = 0
    if n > 1:
        ans += math.factorial(n) // math.factorial(n - 2) // math.factorial(2)
    if m > 1:
        ans += math.factorial(m) // math.factorial(m - 2) // math.factorial(2)
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
        input = """2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """13 3"""
        output = """81"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """0 3"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
