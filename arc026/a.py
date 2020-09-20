import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, a, b = map(int, input().split())
    re_b = min(n, 5)
    print(re_b * b + (n - re_b) * a)

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
        input = """10 5 1"""
        output = """30"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """4 60 7"""
        output = """28"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()