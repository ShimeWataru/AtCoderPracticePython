import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    print(min((b - 1), a - b))


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
        input = """5 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """6 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """90 30"""
        output = """29"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
