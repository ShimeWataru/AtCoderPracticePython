import copy
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    m = sorted(copy.copy(l))
    check = [True] * n
    for i in range(n):
        if not (l[i] == m[i]):
            check[i] = False
    if check.count(False) <= 2:
        print("YES")
    else:
        print("NO")


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
5 2 3 4 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
2 4 3 5 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """7
1 2 3 4 5 6 7"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
