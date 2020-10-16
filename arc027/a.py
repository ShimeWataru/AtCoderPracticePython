import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    h, m = map(int, input().split())
    ans = 0
    if m != 0:
        ans += 60 - m
        h += 1
    ans += (18 - h) * 60
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

    def test_input1(self):
        print("test_input1")
        input = """16 23"""
        output = """97"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """17 59"""
        output = """1"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """13 0"""
        output = """300"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """2 7"""
        output = """953"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
