import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, c, k = map(int, input().split())
    l = sorted([int(input()) for i in range(n)])
    count = 1
    pas = 0
    now = l[0]
    for i in range(len(l)):
        check = now + k
        if pas < c and l[i] <= check:
            pas += 1
        else:
            now = l[i]
            pas = 1
            count += 1
    print(count)


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
        input = """5 3 5
1
2
3
6
12"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6 3 3
7
6
2
8
10
6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
