import sys
from io import StringIO
import unittest
import logging
import math
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += math.sqrt((l[j][0] - l[i][0]) ** 2 +
                             (l[j][1] - l[i][1]) ** 2)
    print(sum * 2 / n)


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
0 0
1 0
0 1"""
        output = """2.2761423749"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
-879 981
-866 890"""
        output = """91.9238815543"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310"""
        output = """7641.9817824387"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
