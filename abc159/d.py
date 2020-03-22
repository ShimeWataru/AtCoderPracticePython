import collections
from functools import reduce
from operator import mul
import math
import copy
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def count_defaultdict(it):
    counter = collections.defaultdict(int)
    for x in it:
        counter[x] += 1
    return dict(counter)


def resolve():
    _ = int(input())
    l = list(map(int, input().split()))
    all_sum = 0
    count = count_defaultdict(l)
    for _, v in count.items():
        all_sum += v * (v - 1) // 2
    for i in range(len(l)):
        if count[l[i]] > 1:
            v = count[l[i]]
            print(all_sum - v * (v-1) // 2 + (v-1) * (v-2)//2)
        else:
            print(all_sum)


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
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
