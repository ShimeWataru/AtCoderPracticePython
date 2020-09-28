import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = list(map(int,input().split()))
    m = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = max(ans, sum(l[:n-i]) + sum(m[n - i - 1:]))
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
        input = """5
3 2 2 4 1
1 2 2 2 1"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 1 1 1
1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
3 3 4 5 4 5 3
5 3 4 4 2 3 2"""
        output = """29"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1
2
3"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()