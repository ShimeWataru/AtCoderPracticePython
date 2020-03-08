import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    ans = 1000000000
    a = 1
    b = n - a
    while (a <= n):
        tmp_ans = 0
        b = n // a
        tmp_ans += n - (a * b)
        tmp_ans += abs(a - b)
        ans = min(ans, tmp_ans)
        a += 1
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

    def test_input1(self):
        print("test_input1")
        input = """26"""
        output = """1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """41"""
        output = """4"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """100000"""
        output = """37"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
