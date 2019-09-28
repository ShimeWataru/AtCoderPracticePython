import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(len(b)):
        c_i = 0
        c_i = min(a[i], b[i])
        c += c_i
        b[i] -= c_i
        c_i_1 = 0
        c_i_1 = min(a[i+1], b[i])
        c += c_i_1
        a[i+1] -= c_i_1
    print(c)


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
        input = """2
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
