import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    w, h, n = map(int, input().split())
    c = [[True] * w for i in range(h)]
    l = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        if l[i][2] == 1:
            for j in range(w):
                for k in range(h):
                    if j < l[i][0]:
                        c[k][j] = False
        elif l[i][2] == 2:
            for j in range(w):
                for k in range(h):
                    if j > l[i][0]-1:
                        c[k][j] = False
        elif l[i][2] == 3:
            for j in range(w):
                for k in range(h):
                    if k < l[i][1]:
                        c[k][j] = False
        else:
            for j in range(w):
                for k in range(h):
                    if k > l[i][1]-1:
                        c[k][j] = False
    for i in range(h):
        ans += c[i].count(True)
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
        input = """5 4 2
2 1 1
3 3 4"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 4 3
2 1 1
3 3 4
1 4 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3"""
        output = """64"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
