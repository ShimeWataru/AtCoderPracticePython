import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    n = int(input())
    print(s[n-1])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """atcoder
3"""
        output = """c"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """beginner
1"""
        output = """b"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """contest
7"""
        output = """t"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """z
1"""
        output = """z"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
