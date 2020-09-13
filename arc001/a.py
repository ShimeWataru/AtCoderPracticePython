import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
from itertools import permutations

def resolve():
    n = int(input())
    l = input()
    choices = [1, 2, 3, 4]
    min_ans = min(l.count(str(x)) for x in choices)
    max_ans = max(l.count(str(x)) for x in choices)
    print(max_ans, min_ans)

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
        input = """9
131142143"""
        output = """4 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
12341234123412341234"""
        output = """5 5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
1111"""
        output = """4 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()