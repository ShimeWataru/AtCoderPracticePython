import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    aa = int(s[:2])
    bb = int(s[2:])
    aa_mm = False
    bb_mm = False
    if 1 <= aa <= 12:
        aa_mm = True
    if 1 <= bb <= 12:
        bb_mm = True

    if aa_mm and bb_mm:
        print("AMBIGUOUS")
    elif bb_mm:
        print("YYMM")
    elif aa_mm:
        print("MMYY")
    else:
        print("NA")


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
        input = """1905"""
        output = """YYMM"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0112"""
        output = """AMBIGUOUS"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1700"""
        output = """NA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
