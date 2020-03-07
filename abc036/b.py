import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [input() for i in range(n)]

    for i in range(n):
        s = ""
        for j in reversed(range(n)):
            s += l[j][i]
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

    def test_input1(self):
        print("test_input1")
        input = """4
ooxx
xoox
xxxx
xxxx"""
        output = """xxxo
xxoo
xxox
xxxx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
