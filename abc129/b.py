import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 9999999999999999
    for i in range(1, n):
        ans = min(ans, abs(sum(l[:i]) - sum(l[i:])))
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
        input = """3
1 2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4
1 3 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8
27 23 76 2 3 5 62 52"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
