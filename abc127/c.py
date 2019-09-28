import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)]
    start = 0
    end = 9999999999
    for i in range(m):
        if l[i][0] > start:
            start = l[i][0]
        if l[i][1] < end:
            end = l[i][1]
    print(max(end-start + 1, 0))


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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
