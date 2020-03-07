import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, s, t = map(int, input().split())
    w = int(input())
    l = [int(input()) for i in range(n-1)]
    ans = 0
    if s <= w <= t:
        ans += 1
    for i in range(n-1):
        w = max(0, w + l[i])
        if s <= w <= t:
            ans += 1
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
        input = """5 60 70
50
10
10
10
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """5 50 100
120
-10
-20
-30
70"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
