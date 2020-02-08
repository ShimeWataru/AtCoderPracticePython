import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)[::-1]
    k = min(k, len(l))
    print(sum(l[k:]))


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
        input = """3 1
4 1 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8 9
7 9 3 2 3 8 4 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3 0
1000000000 1000000000 1000000000"""
        output = """3000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
