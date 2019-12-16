import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, d = map(int, input().split())
    if n % (d*2+1) == 0:
        ans = n // (d * 2 + 1)
    else:
        ans = n // (d * 2 + 1) + 1
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
        input = """6 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """14 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """20 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
