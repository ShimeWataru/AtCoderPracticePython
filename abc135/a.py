import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    ab = (a+b)
    if ab % 2 == 0:
        print(ab // 2)
    else:
        print("IMPOSSIBLE")


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
        input = """2 16"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0 3"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """998244353 99824435"""
        output = """549034394"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
