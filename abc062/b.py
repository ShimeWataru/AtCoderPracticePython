import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    h, w = map(int, input().split())
    l = [input() for _ in range(h)]
    s = "#" * (w + 2)
    print(s)
    for i in range(h):
        m = "#"
        for j in range(w):
            m += str(l[i])[j]
        m += "#"
        print(m)
    print(s)


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
        input = """2 3
abc
arc"""
        output = """#####
#abc#
#arc#
#####"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1 1
z"""
        output = """###
#z#
###"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
