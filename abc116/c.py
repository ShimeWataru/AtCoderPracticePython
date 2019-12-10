import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    m = 0
    tmp_max = l[0]
    check = False
    for i in range(1, n):
        if l[i - 1] > l[i]:
            check = True
        elif check and l[i - 1] < l[i]:
            ans = ans + tmp_max - m
            tmp_max = l[i]
            m = l[i - 1]
            check = False
        elif not(check):
            tmp_max = l[i]
    ans = ans + tmp_max - m
    print(ans)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[: -1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        print("test_input_1")
        input = """4
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
3 1 2 3 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8
4 23 75 0 23 96 50 100"""
        output = """221"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_3")
        input = """21
2 6 7 2 2 8 7 4 7 5 7 7 1 7 7 7 9 6 2 6 6"""
        output = """30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
