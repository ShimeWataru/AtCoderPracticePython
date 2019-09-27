import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, x, y = map(int, input().split())
    min = 999999999999999999999999999999999999
    for i in range(100001):
        price = max(0, x - i) * a + max(0, y - i) * b + (i * 2 * c)
        if price < min:
            min = price
    print(min)


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
        input = """1500 2000 1600 3 2"""
        output = """7900"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1500 2000 1900 3 2"""
        output = """8500"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1500 2000 500 90000 100000"""
        output = """100000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
