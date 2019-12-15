import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    check = True
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            check = False
    if check:
        print("yes")
    else:
        print("no")


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
        input = """uncopyrightable"""
        output = """yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """different"""
        output = """no"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """no"""
        output = """yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
