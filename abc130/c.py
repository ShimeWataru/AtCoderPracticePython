import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    w, h, x, y = map(int, input().split())
    menseki = w * h / 2
    kazu = 0
    if (w / 2 == x) and (h / 2 == y):
        kazu = 1
    print(menseki, kazu)


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
        input = """2 3 1 2"""
        output = """3.000000 0"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 2 1 1"""
        output = """2.000000 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
