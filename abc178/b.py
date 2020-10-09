import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, c, d = map(int, input().split())
    print(max(a*c,a*d,b*c,b*d))

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
        input = """1 2 1 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5 -4 -2"""
        output = """-6"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """-1000000000 0 -1000000000 0"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()