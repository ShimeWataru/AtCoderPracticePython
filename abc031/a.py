import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    print((a+1)*b if a <= b else a*(b+1))


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
        input = """31 87"""
        output = """2784"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """101 65"""
        output = """6666"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """3 3"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
