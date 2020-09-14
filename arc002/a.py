import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    y = int(input())
    print("YES" if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else "NO")

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
        input = """1001"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2012"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2100"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2000"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()