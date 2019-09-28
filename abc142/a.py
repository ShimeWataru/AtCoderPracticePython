import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    num = (n+1) // 2
    print(num / n)


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
        input = """4"""
        output = """0.5000000000"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5"""
        output = """0.6000000000"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1"""
        output = """1.0000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
