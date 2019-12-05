import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, x = map(int, input().split())
    left = 0
    right = 10 ** 9 + 1
    while abs(right-left) != 1:
        mid = (left + right)//2
        money = a*mid+b*int(len(str(mid)))
        if money <= x:
            left = mid
        else:
            right = mid
    print(left)


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
        input = """10 7 100"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 1 100000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1000000000 1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """1234 56789 314159265"""
        output = """254309"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
