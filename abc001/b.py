import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    m = int(input()) / 1000
    if m < 0.1:
        print("00")
    elif m <= 5:
        print(str(int((m * 10)//1)).rjust(2, '0'))
    elif m <= 30:
        print(int((m + 50)//1))
    elif m <= 70:
        m -= 30
        m /= 5
        m += 80
        print(int(m // 1))
    else:
        print(89)


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
        input = """15000"""
        output = """65"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """75000"""
        output = """89"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """200"""
        output = """02"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
