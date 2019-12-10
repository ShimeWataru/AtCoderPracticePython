import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[-2:])
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m < 5:
        print("Heisei")
    elif y == 2019 and m == 4 and d == 30:
        print("Heisei")
    else:
        print("TBD")


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
        input = """2019/04/30"""
        output = """Heisei"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2019/11/01"""
        output = """TBD"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
