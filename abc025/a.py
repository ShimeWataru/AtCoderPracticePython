import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    n = int(input())
    c = 0
    for i in range(5):
        for j in range(5):
            c += 1
            if c == n:
                print(s[i] + s[j])


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
        input = """abcde
8"""
        output = """bc"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """aeiou
22"""
        output = """ue"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """vwxyz
25"""
        output = """zz"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
