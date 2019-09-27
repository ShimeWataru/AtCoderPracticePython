import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    s = input()
    max = 0
    for i in range(n):
        for j in range(i, n):
            c = s.count(s[i:j + 1])
            if (c > 1) and (max < len(s[i:(j + 1)])):
                max = len(s[i:(j + 1)])
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
ababa"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
xy"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """13
strangeorange"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
