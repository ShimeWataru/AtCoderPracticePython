import fractions
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    f = fractions.gcd(a, b)
    f2 = a*b//f
    print(f2)


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
        input = """2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """123 456"""
        output = """18696"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100000 99999"""
        output = """9999900000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
