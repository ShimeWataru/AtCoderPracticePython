import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [list(input().split()) for i in range(n)]
    sum = float(0)
    rate = float(380000)
    for i in range(n):
        if l[i][1] == "JPY":
            sum += float(l[i][0])
        else:
            sum += float(l[i][0]) * rate
    print(sum)


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
        input = """2
10000 JPY
0.10000000 BTC"""
        output = """48000.0"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
100000000 JPY
100.00000000 BTC
0.00000001 BTC"""
        output = """138000000.0038"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
