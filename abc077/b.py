import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = int(input())
    for i in range(s):
        if math.sqrt(s - i).is_integer():
            print(s - i)
            break


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
        input = """10"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """81"""
        output = """81"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """271828182"""
        output = """271821169"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
