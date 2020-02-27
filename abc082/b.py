import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = input()
    b = input()
    a = sorted(a)
    b = sorted(b)[::-1]
    if a < b:
        print("Yes")
    else:
        print("No")


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
        input = """yx
axy"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """ratcode
atlas"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """cd
abc"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """w
ww"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """zzz
zzz"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
