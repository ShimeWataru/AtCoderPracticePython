import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    m = sorted(l)
    max = m[-1][0]
    sub_max = m[-2][0]
    for i in range(n):
        if l[i][0] == max:
            print(sub_max)
        else:
            print(max)


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
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
