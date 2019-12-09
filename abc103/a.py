import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = list(map(int, input().split()))
    l = sorted(l)
    sum = 0
    old = l[0]
    if len(l) == 1:
        print(0)
    else:
        for i in range(1, len(l)):
            sum += l[i] - old
            old = l[i]
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
        input = """1 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """11 5 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100 100 100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
