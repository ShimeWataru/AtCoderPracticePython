import re
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    st = s.find("A")
    en = len(s) - s[::-1].find("Z")
    print(en - st)


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
        input = """QWERTYASDFZXCV"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """ZABCZ"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """HASFJGHOGAKZZFEGA"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
