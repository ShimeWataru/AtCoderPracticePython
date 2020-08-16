import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
import math
def resolve():
    xa, ya, xb, yb, t, v = map(int, input().split())
    n = int(input())
    l = [list(map(int, input().split())) for i in range(n)]
    check = True
    for i in range(n):
        dis1 = math.sqrt((xa-l[i][0]) ** 2 + (ya-l[i][1]) ** 2)
        dis2 = math.sqrt((xb - l[i][0])** 2 + (yb - l[i][1])** 2)
        if (dis1 + dis2) / v <= t:
            check = False
    print("NO" if check else "YES")


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
        input = """1 1 8 2 2 4
1
4 5"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1 1 8 2 2 6
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """1 1 8 2 2 5
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """7 7 1 1 3 4
3
8 1
1 7
9 9"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()