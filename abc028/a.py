import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    if n <= 59:
        print("Bad")
    elif n <= 89:
        print("Good")
    elif n <= 99:
        print("Great")
    else:
        print("Perfect")


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
        input = """80"""
        output = """Good"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """100"""
        output = """Perfect"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """59"""
        output = """Bad"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """95"""
        output = """Great"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
