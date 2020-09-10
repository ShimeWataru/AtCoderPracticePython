import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    if s == "Monday":
        print(5)
    elif s == "Tuesday":
        print(4)
    elif s == "Wednesday":
        print(3)
    elif s == "Thursday":
        print(2)
    elif s == "Friday":
        print(1)
    else:
        print(0)


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
        input = """Monday"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """Saturday"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """Sunday"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """Wednesday"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()