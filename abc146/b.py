import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    s = input()
    l = ""
    for i in range(len(s)):
        if (int(ord(s[i])) + n) >= 91:
            l += chr((int(ord(s[i])) + n) - 26)
        else:
            l += chr(int(ord(s[i])) + n)
    print(l)


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
ABCXYZ"""
        output = """CDEZAB"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0
ABCXYZ"""
        output = """ABCXYZ"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """13
ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        output = """NOPQRSTUVWXYZABCDEFGHIJKLM"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
