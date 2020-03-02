import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    if s == "A":
        print(1)
    elif s == 'B':
        print(2)
    elif s == 'C':
        print(3)
    elif s == 'D':
        print(4)
    elif s == 'E':
        print(5)


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
        input = """A"""
        output = """1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """B"""
        output = """2"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """C"""
        output = """3"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """D"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
