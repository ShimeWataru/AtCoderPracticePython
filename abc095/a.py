import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = (input().count("o"))
    print(700 + 100 * int(s))


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
        input = """oxo"""
        output = """900"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """ooo"""
        output = """1000"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """700"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
