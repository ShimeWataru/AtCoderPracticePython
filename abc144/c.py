import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def divisor(n):
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass


def resolve():
    n = int(input())
    l = sorted(divisor(n))
    if len(l) % 2 == 1:
        print(l[(len(l) // 2)] * 2 - 2)
    else:
        print(l[(len(l)//2 - 1)] + l[(len(l)//2)] - 2)


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
        input = """49"""
        output = """12"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """50"""
        output = """13"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10000000019"""
        output = """10000000018"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
