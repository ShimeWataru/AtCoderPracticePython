import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = int((n ** (1 / 2))//1)
    b = 1
    print(a, b)
    for i in reversed(range(1, a)):
        if n % i == 0:
            a = i
            b = n // i

    print(abs(a-b) + (n - a*b))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """26"""
        output = """1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """41"""
        output = """4"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """100000"""
        output = """37"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
