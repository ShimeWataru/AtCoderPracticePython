import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = list(map(int, input().split()))
    rgb = l[0] * 100 + l[1] * 10 + l[2]
    if rgb % 4 == 0:
        print("YES")
    else:
        print("NO")


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
        input = """4 3 2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 3 4"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
