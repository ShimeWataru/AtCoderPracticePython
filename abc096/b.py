import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    k = int(input())
    ans = sum([max(a, b, c) * 2 ** k, a, b, c]) - max(a, b, c)
    print(ans)


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
        input = """5 3 11
1"""
        output = """30"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 3 4
2"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
