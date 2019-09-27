import numpy as np
import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    # n, m = map(int, input().split())
    # a = np.array(list(map(int, input().split())))
    # for i in range(m):
    #     a[np.argmax(a)] /= 2
    # b = [abc // 1 for abc in a]
    # print(np.sum(b))
    n, m = map(int, input().split())
    sum = 0
    a = np.array(list(map(int, input().split())))
    for i in range(m):
        np.sort(a)[::-1]
        a[0] /= 2
    for i in range(n):
        sum += a[i] // 1
    print(sum)


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
        input = """3 3
2 13 8"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 4
1 9 3 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 100000
1000000000"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """9500000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
