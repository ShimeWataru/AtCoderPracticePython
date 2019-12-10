import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    print(a*b/2)


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
        input = """3 4 5"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 12 13"""
        output = """30"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """45 28 53"""
        output = """630"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
