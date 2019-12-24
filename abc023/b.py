import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    s = input()
    c = n // 2
    check = True
    if n == 1:
        if s[c] == "b":
            print(0)
        else:
            print(-1)
    elif n > 3 and not((n - 1) % 2 == 0):
        print(-1)
    elif s[c] == "b":
        for i in range(n // 2 + 1):
            if i > 0 and i % 3 == 0:
                if not (s[c - i] == s[c + i] == "b"):
                    check = False
            if i > 0 and i % 3 == 1:
                if not (s[c - i] == "a" and s[c + i] == "c"):
                    check = False
            if i > 0 and i % 3 == 2:
                if not (s[c - i] == "c" and s[c + i] == "a"):
                    check = False
        if check:
            print(c)
        else:
            print(-1)
    else:
        print(-1)


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
        input = """3
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """6
abcabc"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """7
atcoder"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """19
bcabcabcabcabcabcab"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
