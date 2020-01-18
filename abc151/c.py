import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(input().split()) for i in range(m)]
    ac = [False] * n
    count = [0] * n
    sum_wa = 0
    for i in range(len(l)):
        # print(l[i][0], l[i][1])
        if l[i][1] == "WA" and ac[int(l[i][0]) - 1] == False:
            count[int(l[i][0]) - 1] += 1
        elif l[i][1] == "AC":
            sum_wa += count[int(l[i][0]) - 1]
            count[int(l[i][0]) - 1] = 0
            ac[int(l[i][0]) - 1] = True
    print(ac.count(True), sum_wa)


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
        input = """2 5
1 WA
1 AC
2 WA
2 AC
2 WA"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """100000 3
7777 AC
7777 AC
7777 AC"""
        output = """1 0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 0"""
        output = """0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
