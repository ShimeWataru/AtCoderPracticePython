import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = list(map(int, input().split()))
    l = sorted(l)
    print(l[0] + l[1])


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
        input = """700 600 780"""
        output = """1300"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10000 10000 10000"""
        output = """20000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
