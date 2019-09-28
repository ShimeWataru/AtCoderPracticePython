import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def answer(x, i, j):
    lcm = (i * j) // math.gcd(i, j)
    xi = x // i
    xj = x // j
    xlcm = x // lcm
    return x - xi - xj + xlcm


def resolve():
    a, b, c, d = map(int, input().split())
    ans = answer(b, c, d) - answer(a-1, c, d)
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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
