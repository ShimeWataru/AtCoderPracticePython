import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = list(map(int, input().split()))
    l = sorted(l)
    print(int(str(l[2]) + str(l[1])) + l[0])


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
        input = """1 5 2"""
        output = """53"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9 9 9"""
        output = """108"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 6 7"""
        output = """82"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
