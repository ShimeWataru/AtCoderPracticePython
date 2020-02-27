import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    print((a-c)//(b+c))


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
        input = """13 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """12 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100000 1 1"""
        output = """49999"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """64146 123 456"""
        output = """110"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """64145 123 456"""
        output = """109"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
