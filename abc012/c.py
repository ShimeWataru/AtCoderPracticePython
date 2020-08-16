import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = 2025 - int(input())
    for i in range(1,10):
        for j in range(1, 10):
            if i * j == n:
                print(i,"x",j)


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
        input = """2013"""
        output = """2 x 6
3 x 4
4 x 3
6 x 2"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """2024"""
        output = """1 x 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()