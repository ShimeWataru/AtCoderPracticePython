import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    d, x = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    sum = 0
    for i in range(n):
        day_i = 1
        while (day_i <= d):
            sum += 1
            day_i += l[i]
    print(sum + x)


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
7 1
2
5
10"""
        output = """8"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
8 20
1
10"""
        output = """29"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
30 44
26
18
81
18
6"""
        output = """56"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
