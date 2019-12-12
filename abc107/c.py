import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 9999999999999
    for i in range(len(l) - k + 1):
        min_l = min(0, l[i])
        max_l = max(0, l[i+k-1])
        min_abs = min(abs(min_l), abs(max_l))
        max_abs = max(abs(min_l), abs(max_l))
        ans = min(ans, min_abs * 2 + max_abs)
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
        input = """5 3
-30 -10 10 20 50"""
        output = """40"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 2
10 20 30"""
        output = """20"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 1
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """8 5
-9 -7 -4 -3 1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
