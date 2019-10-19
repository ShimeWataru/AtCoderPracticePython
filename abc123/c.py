import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [int(input()) for i in range(5)]
    print(4 + (-(-n//min(l))))


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
3
2
4
3
5"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10
123
123
123
123
123"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10000000007
2
3
5
7
11"""
        output = """5000000008"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
