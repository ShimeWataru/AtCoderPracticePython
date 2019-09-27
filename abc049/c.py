import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    S = input()
    S = S[::-1]
    pattern = ["dream", "dreamer", "erase", "eraser"]
    check = True
    while check:
        check = False
        for i in range(len(pattern)):
            if S.startswith(pattern[i][::-1]):
                S = S[len(pattern[i]):]
                check = True
    if len(S) == 0:
        print("YES")
    else:
        print("NO")


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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
