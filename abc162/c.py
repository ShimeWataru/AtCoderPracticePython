import sys
from io import StringIO
import unittest
import logging
import fractions
logging.basicConfig(level=logging.DEBUG)
from math import gcd

def resolve():
    n = int(input())
    ans = 0
    for i in range(1,n + 1):
        for j in range(1, n + 1):
            f = gcd(i, j)
            for k in range(1, n + 1):
                ans += gcd(f, k)
    print(ans)

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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()