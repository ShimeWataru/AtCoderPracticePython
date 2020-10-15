import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l, r = map(int, input().split())
    l_l = list(map(int,input().split()))
    l_r = list(map(int, input().split()))
    ans = 0
    for i in range(l):
        if l_l[i] in l_r:
            ans += 1
            l_r.remove(l_l[i])
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
        input = """3 3
20 21 22
30 22 15"""
        output = """1"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """3 4
10 11 10
12 10 11 25"""
        output = """2"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """5 5
10 10 10 10 10
10 10 10 10 10"""
        output = """5"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """5 5
10 11 12 13 14
30 31 32 33 34"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()