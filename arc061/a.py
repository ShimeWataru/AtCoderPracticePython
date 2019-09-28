import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    S = input()
    sum = 0
    for j in range(2**(len(S)-1)):
        shiki = ""
        for i in range(len(S)):
            bin_str = str(format(j, 'b').rjust(10, '0'))
            shiki += S[i]
            if bin_str[-i - 1] == "1":
                shiki = shiki + "+"
        sum += eval(shiki)
    print(sum)


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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
