import re
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    max_re = 0
    for i in range(len(s)):
        tar_s = s[i:]
        tar_s = re.search(r'(A|T|C|G)*', tar_s).group()
        max_re = max(max_re, len(tar_s))
    print(max_re)


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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """HATAGAYA"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """SHINJUKU"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
