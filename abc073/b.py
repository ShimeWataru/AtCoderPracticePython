import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    sum = 0
    for i in range(n):
        sum += l[i][1] - l[i][0] + 1
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
        input = """1
24 30"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
6 8
3 3"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
