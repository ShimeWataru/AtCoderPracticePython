import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    pass


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
        input = """8 7
1 2
2 3
2 4
5 6
6 7
6 8
7 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """5 1
1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """11 11
1 2
1 3
2 4
3 5
4 6
5 7
6 8
7 9
8 10
9 11
10 11"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
