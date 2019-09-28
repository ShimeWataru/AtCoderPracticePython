import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l, r = map(int, input().split())
    ans = 9999
    r = min(r, l+4038)
    for i in range(l, r):
        for j in range(i + 1, r+1):
            if (i * j) % 2019 < ans:
                ans = (i * j) % 2019
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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
