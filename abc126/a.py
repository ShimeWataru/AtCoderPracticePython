import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    s = input()
    ans = ""
    for i in range(n):
        if i == k - 1:
            ans += s[i].lower()
        else:
            ans += s[i]
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
        input = """3 1
ABC"""
        output = """aBC"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 3
CABA"""
        output = """CAbA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
