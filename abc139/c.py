import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = input()
    a = list(map(int, input().split()))
    max = 0
    target = a[0]
    c = 0
    for i in range(1, len(a)):
        if target >= a[i]:
            c += 1
        else:
            c = 0
        if max < c:
            max = c
        target = a[i]
    print(max)


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
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
