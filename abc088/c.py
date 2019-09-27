
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    cube = [list(map(int, input().split())) for i in range(3)]
    a = True
    x = [0] * 3
    y = [0] * 3
    x[0] = 0
    y[0] = cube[0][0] - x[0]
    y[1] = cube[0][1] - x[0]
    y[2] = cube[0][2] - x[0]
    x[1] = cube[1][0] - y[0]
    x[2] = cube[2][0] - y[0]

    for i in range(3):
        for j in range(3):
            if not (x[i] + y[j] == cube[i][j]):
                a = False
    if a:
        print("Yes")
    else:
        print("No")


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
        input = """1 0 1
2 1 2
1 0 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 2 2
2 1 2
2 2 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """0 8 8
0 8 8
0 8 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """1 8 6
2 9 7
0 7 7"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
