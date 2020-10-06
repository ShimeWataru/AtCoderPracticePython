import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x, y = map(int, input().split())
    k = int(input())
    r = k if y >= k else y
    ans = x + r - (k - r)
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
    def test_input1(self):
        print("test_input1")
        input = """3 2
1"""
        output = """4"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """3 2
4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """3 2
5"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()