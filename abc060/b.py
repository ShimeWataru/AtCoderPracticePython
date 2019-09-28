import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    check = False
    i = a
    while i <= a * b:
        if i % b == c:
            check = True
        i = i + a
    if check:
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
        input = """7 5 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 2 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 100 97"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """40 98 58"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """77 42 36"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
