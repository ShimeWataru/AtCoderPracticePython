import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = input().split()
    print(a[0].upper() + b[0].upper() + c[0].upper())


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
        input = """atcoder beginner contest"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """resident register number"""
        output = """RRN"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """k nearest neighbor"""
        output = """KNN"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """async layered coding"""
        output = """ALC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
