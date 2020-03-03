import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]
    p = [list(map(int, input().split())) for i in range(m)]

    for i in range(n):
        min_l = 1000000000
        index = 0
        for j in range(m):
            d = abs(l[i][0] - p[j][0]) + abs(l[i][1] - p[j][1])
            if min_l > d:
                min_l = d
                index = j
        print(index + 1)


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
2 0
0 0
-1 0
1 0"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5"""
        output = """3
1
2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000"""
        output = """5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
