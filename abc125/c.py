import copy
import fractions
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    sum = 0
    if len(l) == 2:
        print(max(l[0], l[1]))
        exit()
    else:
        for i in range(n):
            ll = copy.deepcopy(l)
            ll.pop(i)
            ans = ll[0]
            for j in range(1, len(ll)):
                ans = fractions.gcd(ans, ll[j])
                if sum < ans:
                    sum = ans
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
        input = """3
7 6 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
