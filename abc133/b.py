import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, d = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]

    ans = 0

    for i in range(n - 1):
        tmp = 0
        for j in range(i + 1, n):
            tmp = 0
            for k in range(d):
                tmp += (l[i][k] - l[j][k]) ** 2
            if math.sqrt(tmp).is_integer():
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

    def test_input_1(self):
        print("test_input_1")
        input = """3 2
1 2
5 5
-2 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 1
1
2
3
4
5"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
