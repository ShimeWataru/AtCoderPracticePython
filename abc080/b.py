import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = a
    f = 0
    while a > 0:
        f += a % 10
        a = a // 10
    if b % f == 0:
        print("Yes")
    else:
        print("No")


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
        input = """12"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """57"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """148"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
