import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
from itertools import permutations

def resolve():
    a = map(int, input().split())
    p, q, r = map(int, input().split())
    print(max(x // p * (y // q) * (z // r) for x, y, z in permutations(a)))

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
        input = """10 10 10
1 1 1"""
        output = """1000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 3 1
2 1 1"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 10 3
2 5 3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """8 8 8
1 1 9"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()