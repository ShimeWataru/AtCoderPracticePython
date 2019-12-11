import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    min_ab = min(a, b)
    min_cd = min(c, d)
    print(min_ab + min_cd)


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
        input = """600
300
220
420"""
        output = """520"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """555
555
400
200"""
        output = """755"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """549
817
715
603"""
        output = """1152"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
