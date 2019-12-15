import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [int(input()) for _ in range(n)]
    l = sorted(l)
    sum_l = sum(l)
    ans = 0

    if not (sum_l % 10 == 0):
        print(sum_l)
    else:
        for i in range(n):
            tmp = sum_l - l[i]
            if not (tmp % 10 == 0):
                ans = max(ans, tmp)

        for i in range(n):
            for j in range(i, n):
                tmp = sum_l - l[i] - l[j]
                if not (tmp % 10 == 0):
                    ans = max(ans, tmp)
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
5
10
15"""
        output = """25"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
10
10
15"""
        output = """35"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3
10
20
30"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
