import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n + 1):
        count = 0
        deme = i
        while i < k:
            i = i * 2
            count += 1
        sum += (1 / n) * (1 / 2)**count
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
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
