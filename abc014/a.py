import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = int(input())
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)


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
        input = """7
3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """5
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """1
100"""
        output = """99"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """25
12"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
