import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 1
    if 0 in l:
        print(0)
    else:
      for i in range(n):
          ans *= l[i]
          if ans > 1000000000000000000:
            ans = -1
            break
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
        input = """2
1000000000 1000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
101 9901 999999000001"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """31
4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()