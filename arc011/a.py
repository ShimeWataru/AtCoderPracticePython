import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    m, n, a = map(int, input().split())
    ans = 0
    while (True):
        ans += a - a % m
        a = (a // m * n) + a % m
        if a < m:
            break
    print(ans + a)

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
        input = """2 1 8"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 4 30"""
        output = """62"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 99 1000"""
        output = """90199"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()