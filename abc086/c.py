import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [list(map(int, input().split())) for i in range(n)]
    check = True
    for i in range(len(l)):
        if not((l[i][0] >= l[i][1] + l[i][2]) and (l[i][0] % 2 == ((l[i][1] + l[i][2]) % 2))):
            check = False
    if check:
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
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
