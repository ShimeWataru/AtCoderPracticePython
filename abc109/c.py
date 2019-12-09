import fractions
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    if len(l) == 1:
        print(abs(l[0] - x))
    elif len(l) == 2:
        print(fractions.gcd(abs(l[0] - x), abs(l[1] - x)))
    else:
        ans = fractions.gcd(abs(l[0] - x), abs(l[1] - x))
        for i in range(2, n):
            ans = fractions.gcd(ans, abs(l[i] - x))
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
        input = """3 3
1 7 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 81
33 105 57"""
        output = """24"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 1
1000000000"""
        output = """999999999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
