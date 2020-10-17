import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
from sys import stdin

def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    cnt = [0] * (100000 + 1)
    ans = 0
    for i in range(n):
        cnt[l[i]] += 1
    for i in range(1, 100000):
        tmp = cnt[i - 1] + cnt[i] + cnt[i + 1]
        ans = max(ans, tmp)
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
        input = """7
3 1 4 1 5 9 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
0 1 2 3 4 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
99999"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2
999999999 1000000000"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()