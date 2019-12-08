import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():

    n = int(input())
    l = list(map(bin, input().split()))
    sum = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum += (l[i] ^ l[j])
    print(sum % (10 ** 9 + 7))


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
1 2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """237"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10
3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820"""
        output = """103715602"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
