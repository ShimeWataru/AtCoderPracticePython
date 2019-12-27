import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, x = map(int, input().split())
    l = [int(input()) for i in range(n)]
    l = sorted(l)
    x -= sum(l)
    print(n + x // l[0])


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
        input = """3 1000
120
100
140"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 360
90
90
90
90"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 3000
150
130
150
130
110"""
        output = """26"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
