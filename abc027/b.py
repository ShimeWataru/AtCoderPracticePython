import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    check = [False] * (n - 1)
    if sum(l) % n == 0:
        h = sum(l) // n
        y = 0
        for i in range(n):
            y += l[i] - h
            if y != 0:
                check[i] = True
        print(check.count(True))
    else:
        print(-1)


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
        input = """3
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """5
2 0 0 0 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """2
0 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """4
0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
