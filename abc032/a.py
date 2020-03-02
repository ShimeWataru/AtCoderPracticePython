import fractions
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = int(input())
    n = int(input())
    for i in range(n, 20001):
        if i % a == 0 and i % b == 0:
            print(i)
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

    def test_input1(self):
        print("test_input1")
        input = """2
3
8"""
        output = """12"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """2
2
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """12
8
25"""
        output = """48"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
