import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    ans = 0
    for _ in range(2):
        if a >= b:
            ans += a
            a -= 1
        else:
            ans += b
            b -= 1
    print(ans)


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
        input = """5 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 6"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
