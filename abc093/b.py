import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, k = map(int, input().split())
    print_max = 0
    for i in range(a, a + k):
        if a <= i <= b:
            print(i)
            print_max = i
    for i in range(b - k + 1, b + 1):
        if print_max < i <= b:
            print(i)


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
        input = """3 8 2"""
        output = """3
4
7
8"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 8 3"""
        output = """4
5
6
7
8"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2 9 100"""
        output = """2
3
4
5
6
7
8
9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
