import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, t = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]
    l.sort(key=lambda x: x[1])
    ans = 9999999999
    if l[0][1] > t:
        print("TLE")
    else:
        for i in range(n):
            if l[i][1] <= t:
                ans = min(ans, l[i][0])
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
        input = """3 70
7 60
1 80
4 50"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 1000
2 4
3 1000
4 500"""
        output = """TLE"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 9
25 8
5 9
4 10
1000 1000
6 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
