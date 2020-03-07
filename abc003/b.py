import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    m = input()
    check = True
    for i in range(len(s)):
        if s[i] == m[i]:
            next
        elif s[i] == "@" and m[i] in "atcoder":
            next
        elif m[i] == "@" and s[i] in "atcoder":
            next
        else:
            check = False
    if check:
        print("You can win")
    else:
        print("You will lose")


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
        input = """ch@ku@ai
choku@@i"""
        output = """You can win"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """aoki
@ok@"""
        output = """You will lose"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """arc
abc"""
        output = """You will lose"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
