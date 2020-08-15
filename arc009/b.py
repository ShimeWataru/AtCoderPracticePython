import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l = list(map(int, input().split()))
    n = int(input())
    nums = []
    for i in range(n):
        num = input()
        transform_num = 0
        len_num = len(num)
        for j in range(len_num):
            transform_num += l.index(int(num[j])) * 10 ** (len_num - j - 1)
        nums.append([int(num), transform_num])
    nums = sorted(nums, key=lambda x: x[1])
    for i in range(len(nums)):
        print(nums[i][0])


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
        input = """0 8 1 3 5 4 9 7 6 2
10
1
2
3
4
5
6
7
8
9
10"""
        output = """8
1
3
5
4
9
7
6
2
10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0 9 8 7 6 5 4 3 2 1
3
13467932
98738462
74392"""
        output = """74392
98738462
13467932"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 1 2 3 4 5 6 7 8 9
4
643
1234
43
909"""
        output = """43
643
909
1234"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """0 7 4 3 9 5 6 2 1 8
2
333
333"""
        output = """333
333"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """0 2 4 6 8 1 3 5 7 9
1
10"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()