import collections
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    S = collections.Counter(l)
    S = sorted(S.values())
    print(sum(S[:len(S)-k]))


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
        input = """5 2
1 1 2 2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 4
1 1 2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 3
5 1 3 2 4 1 1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
