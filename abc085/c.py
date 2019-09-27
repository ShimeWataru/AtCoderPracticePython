import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    N, Y = map(int, input().split())
    for i in range(N + 1):
        for j in range(N - i + 1):
            if i * 10000 + j * 5000 + (N - i - j) * 1000 == Y:
                print(i, j, N - i - j)
    print(-1, -1, -1)


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
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
