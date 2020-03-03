import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    c = [1, 3, 5, 7, 8, 10, 12]
    d = [4, 6, 9, 11]
    e = [2]
    if ((a in c) and (b in c)) or ((a in d) and (b in d)) or ((a in e) and (b in e)):
        print("Yes")
    else:
        print("No")


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
        input = """1 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 4"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
