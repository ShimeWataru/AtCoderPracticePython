import itertools
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    all_n = []
    for i in itertools.permutations(a):
        all_n.append(int("".join(map(str, i))))
    all_n = sorted(all_n)
    a = int("".join(map(str, a)))
    b = int("".join(map(str, b)))
    num_a = 0
    num_b = 0
    for i in range(len(all_n)):
        if i == a:
            num_a = i + 1
        if i == b:
            num_b = i + 1
    print(all_n)


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
        input = """3
1 3 2
3 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1"""
        output = """17517"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3
1 2 3
1 2 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
