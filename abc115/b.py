import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [int(input()) for i in range(n)]
    l = sorted(l)
    print(sum(l) - l[-1]//2)


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
        input = """3
4980
7980
6980"""
        output = """15950"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4
4320
4320
4320
4320"""
        output = """15120"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
