import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    h, n = map(int, input().split())
    l = list(map(int, input().split()))
    sum_l = sum(l)
    if h <= sum_l:
        print("Yes")
    else:
        print("No")


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
        input = """10 3
4 5 6"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """20 3
4 5 6"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """210 5
31 41 59 26 53"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """211 5
31 41 59 26 53"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
