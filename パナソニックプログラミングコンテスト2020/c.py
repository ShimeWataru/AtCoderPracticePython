
import decimal
import sys
from io import StringIO
import unittest
import logging
import math
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    print("Yes" if math.pow(a, 0.5) + math.pow(b, 0.5)
          < math.pow(c, 0.5) else "No")


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
        input = """4 4 16"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
