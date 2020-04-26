import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    ans = n - sum(l)
    if ans >= 0:
      print(ans)
    else:
      print(-1)

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
        input = """41 2
5 6"""
        output = """30"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 2
5 6"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """11 2
5 6"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """314 15
9 26 5 35 8 9 79 3 23 8 46 2 6 43 3"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()