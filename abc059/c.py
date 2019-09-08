
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = input()
    b = list(map(int, input().split()))
    c = round(sum(b) / len(b))
    s = 0
    for i in range(len(b)):
        s += ((b[i] - c) ** 2)
    print(s)


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
        input = """2
4 8"""
        output = """8"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3
4 2 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """4
-100 -100 -100 -100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
