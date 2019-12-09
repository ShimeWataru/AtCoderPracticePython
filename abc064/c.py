import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    c = [False] * 8
    red = 0
    for i in range(n):
        if l[i] <= 399:
            c[0] = True
        elif l[i] <= 799:
            c[1] = True
        elif l[i] <= 1199:
            c[2] = True
        elif l[i] <= 1599:
            c[3] = True
        elif l[i] <= 1999:
            c[4] = True
        elif l[i] <= 2399:
            c[5] = True
        elif l[i] <= 2799:
            c[6] = True
        elif l[i] <= 3199:
            c[7] = True
        else:
            red += 1
    ans_min = max(1, c.count(True))
    ans_max = c.count(True) + red
    print(ans_min, ans_max)


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
        input = """4
2100 2500 2700 2700"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
1100 1900 2800 3200 3200"""
        output = """3 5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990"""
        output = """1 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
