import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    l.sort(key=lambda x: x[0])
    num = 0
    ansum = 0
    for i in range(n):
        if num + l[i][1] < m:
            ansum += l[i][0] * l[i][1]
            num += l[i][1]
        else:
            ansum += l[i][0] * (m - num)
            break
    print(ansum)


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
4 9
2 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 30
6 18
2 5
3 10
7 9"""
        output = """130"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 100000
1000000000 100000"""
        output = """100000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
