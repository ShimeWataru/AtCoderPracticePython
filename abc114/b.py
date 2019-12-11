import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    min = 999
    for i in range(len(s)-2):
        if abs(int(s[i:i + 3]) - 753) < min:
            min = abs(int(s[i:i + 3]) - 753)
    print(min)


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
        input = """1234567876"""
        output = """34"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """35753"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1111111111"""
        output = """642"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
