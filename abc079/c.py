import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, d = input()
    kigou = ["+", "-"]
    for i in range(8):
        bin_str = str(format(i, 'b').rjust(10, '0'))
        soeji_01 = int(bin_str[-1])
        soeji_02 = int(bin_str[-2])
        soeji_03 = int(bin_str[-3])
        shiki = "" + a + kigou[soeji_01] + b + \
            kigou[soeji_02] + c + kigou[soeji_03] + d
        if eval(shiki) == 7:
            print(shiki+"=7")


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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
