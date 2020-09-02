import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    a = 0
    if 400 <= n <= 599:
        a = 8
    elif 600 <= n <= 799:
        a = 7
    elif 800 <= n <= 999:
        a = 6
    elif 1000 <= n <= 1199:
        a = 5
    elif 1200 <= n <= 1399:
        a = 4
    elif 1400 <= n <= 1599:
        a = 3
    elif 1600 <= n <= 1799:
        a = 2
    else:
        a = 1
    print(a)

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
        input = """725"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1600"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()