import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    w, a, b = map(int, input().split())
    migi = b - (a + w)
    hidari = b + w - a
    if b <= (a + w) and abs(migi) <= w:
        migi = 0
    elif a <= (b + w) and abs(hidari) <= w:
        hidari = 0
    print(min(abs(migi), abs(hidari)))


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
        input = """3 2 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 1 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 10 1"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
