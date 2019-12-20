import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    k = int(input())
    renzoku = 0
    for i in range(len(s)):
        if s[i] == "1":
            renzoku += 1
        else:
            break
    if renzoku >= k:
        print(1)
    else:
        print(s[renzoku])


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
        input = """1214
4"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
157"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """299792458
9460730472580800"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
