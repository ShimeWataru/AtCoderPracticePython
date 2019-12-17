import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, p = map(int, input().split())
    print((3*n+p)//2)


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
        input = """1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """32 21"""
        output = """58"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
