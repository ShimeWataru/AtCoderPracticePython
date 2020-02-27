import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)
    l = l[-k:]
    ans = 0
    for i in range(len(l)):
        ans = (ans + l[i]) / 2
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
        input = """2 2
1000 1500"""
        output = """1000.000000"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 1
1000 1500"""
        output = """750"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 5
2604 2281 3204 2264 2200 2650 2229 2461 2439 2211"""
        output = """2820.031250000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
