import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    at = l[0]
    ans = 0
    max_i = 0
    max_l = sum(l[:k])
    hikaku = sum(l[:k])
    if k == 1:
        a = max(l)
        print(a * (a + 1) / 2 / a)
    else:
        for i in range(1, n - k + 1):
            hikaku = hikaku - at + l[i + k - 1]
            at = l[i]
            if max_l < hikaku:
                max_i = i
                max_l = hikaku
        for i in range(k):
            a = l[max_i + i]
            ans += a * (a + 1) / 2 / a
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
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
