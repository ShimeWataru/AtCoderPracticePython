import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    b = []
    for i in range(n):
        h, s = map(int, input().split())
        b.append((h, s))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """4
5 6
12 4
14 7
21 2"""
        output = """23"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """6
100 1
100 1
100 1
100 1
100 1
1 30"""
        output = """105"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
