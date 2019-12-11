import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = input().split()
    ans = a[0] + b[0] + c[0]
    print(ans)


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
        input = """AtCoder Beginner Contest"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """AtCoder Snuke Contest"""
        output = """ASC"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """AtCoder X Contest"""
        output = """AXC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
