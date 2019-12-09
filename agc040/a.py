import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    for_l = [0] * (len(s) + 1)
    for_r = [0] * (len(s) + 1)
    l = [0] * (len(s) + 1)
    for i in range(1, len(for_l)):
        if s[i - 1] == "<":
            for_l[i] = for_l[i - 1] + 1
    for i in range(1, len(for_l)):
        if s[-i] == ">":
            for_r[-i-1] = for_r[-i] + 1
    for i in range(len(for_l)):
        l[i] = max(for_l[i], for_r[i])
    print(sum(l))


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
        input = """<>>"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """<>>><<><<<<<>>><"""
        output = """28"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
