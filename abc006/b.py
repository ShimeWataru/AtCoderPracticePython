import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [0] * (n + 1)
    if n == 1 or n == 2:
        print(0)
    else:
        l[3] = 1
        for i in range(4, n + 1):
            l[i] = (l[i - 1] + l[i - 2] + l[i - 3]) % 10007
        print(l[n])


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
        input = """7"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100000"""
        output = """7927"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
