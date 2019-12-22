import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def aaa(x):
    if x < 2:
        return 1
    else:
        return x * aaa(x - 2)


def resolve():
    n = int(input())
    ans = aaa(n)
    print(ans)


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
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_3")
        input = """1000"""
        output = """124999999999999995"""
        self.assertIO(input, output)

    # def test_input_3(self):
    #     print("test_input_3")
    #     input = """1000000000000000000"""
    #     output = """124999999999999995"""
    #     self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
