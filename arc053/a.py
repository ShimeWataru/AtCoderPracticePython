import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    h, w = map(int, input().split())
    print((h-1) * w + h * (w-1))


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
        input = """2 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """4 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
