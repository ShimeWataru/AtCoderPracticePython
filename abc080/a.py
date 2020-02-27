import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    print(min(a * b, c))


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
        input = """7 17 120"""
        output = """119"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 20 100"""
        output = """100"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 18 100"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
