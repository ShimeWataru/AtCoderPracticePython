import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(input().split())
    if 'Y' in l:
        print("Four")
    else:
        print("Three")


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
        input = """6
G W Y P Y W"""
        output = """Four"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9
G W W G P W P G G"""
        output = """Three"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8
P Y W G Y W Y Y"""
        output = """Four"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
