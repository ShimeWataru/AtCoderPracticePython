import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    if s == "SUN":
        print(7)
    elif s == "MON":
        print(6)
    elif s == "TUE":
        print(5)
    elif s == "WED":
        print(4)
    elif s == "THU":
        print(3)
    elif s == "FRI":
        print(2)
    elif s == "SAT":
        print(1)


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
        input = """SAT"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """SUN"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
