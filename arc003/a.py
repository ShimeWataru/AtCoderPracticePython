import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = input()
    sum_gpa = 0
    sum_gpa += l.count("A") * 4
    sum_gpa += l.count("B") * 3
    sum_gpa += l.count("C") * 2
    sum_gpa += l.count("D") * 1
    print(sum_gpa / n)

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
        input = """34
ABABAAABACDDDABADFFABABDABFAAABFAA"""
        output = """2.79411764705882"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
FFFFF"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()