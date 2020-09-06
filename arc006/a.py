import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    e = list(map(int, input().split()))
    b = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    b_c = b in l
    for i in range(len(l)):
        if l[i] in e:
            cnt += 1
    if cnt == 6:
        print("1")
    elif cnt == 5 and b_c:
        print("2")
    elif cnt == 5:
        print("3")
    elif cnt == 4:
        print("4")
    elif cnt == 3:
        print("5")
    else:
        print("0")



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
        input = """1 2 3 4 5 6
7
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0 1 3 5 7 9
4
0 2 4 6 8 9"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 2 6 7 8 9
4
0 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1 3 5 6 7 8
9
3 5 6 7 8 9"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """0 1 3 4 5 7
8
2 3 5 7 8 9"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()