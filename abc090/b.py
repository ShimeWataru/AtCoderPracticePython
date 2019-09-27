import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    c = 0
    for i in range(a, b + 1):
        s = str(i)
        if s == s[::-1]:
            c += 1
    print(c)


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
        input = """11009 11332"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """31415 92653"""
        output = """612"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
