import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(m)]
    count_ball = [1] * n
    check = [False] * n
    check[0] = True
    for i in range(m):
        count_ball[l[i][0] - 1] -= 1
        count_ball[l[i][1]-1] += 1
        if check[l[i][0]-1]:
            check[l[i][1]-1] = True
        if count_ball[l[i][0]-1] == 0:
            check[l[i][0]-1] = False
    print(check.count(True))


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
        input = """3 2
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
