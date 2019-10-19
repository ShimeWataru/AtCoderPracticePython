import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = [int(input()) for i in range(6)]
    if l[-2] - l[0] <= l[-1]:
        print("Yay!")
    else:
        print(":(")


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
        input = """1
2
4
8
9
15"""
        output = """Yay!"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """15
18
26
35
36
18"""
        output = """:("""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
