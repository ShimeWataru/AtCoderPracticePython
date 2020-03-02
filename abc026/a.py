import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = n // 2
    b = n - a
    print(a*b)


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
        input = """10"""
        output = """25"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """60"""
        output = """900"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
