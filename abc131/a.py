import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    tmp = s[0]
    check = True
    for i in range(1, len(s)):
        if tmp == s[i]:
            check = False
        tmp = s[i]
    if check:
        print("Good")
    else:
        print("Bad")


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
        input = """3776"""
        output = """Bad"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8080"""
        output = """Good"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1333"""
        output = """Bad"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """0024"""
        output = """Bad"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
