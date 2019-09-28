import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(1, n - 1):
        if (not (min(l[i - 1], l[i], l[i+1]) == l[i])) and (not (max(l[i - 1], l[i], l[i+1]) == l[i])):
            c += 1
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
        input = """5
1 3 5 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9
9 6 3 2 5 8 7 4 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
