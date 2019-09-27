import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    if a % 10 == 0:
        print(10)
    else:
        c = 0
        while (a > 0):
            c += a % 10
            a = a//10
        print(c)


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
        input = """15"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """100000"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
