import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m, x, y = map(int, input().split())
    l_a = list(map(int, input().split()))
    l_b = list(map(int, input().split()))
    l_a.append(x)
    l_b.append(y)
    l_a = sorted(l_a)
    l_b = sorted(l_b)
    if l_a[-1] < l_b[0]:
        print("No War")
    else:
        print("War")


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
        input = """3 2 10 20
8 15 13
16 22"""
        output = """No War"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 2 -48 -1
-20 -35 -91 -23
-22 66"""
        output = """War"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 3 6 8
-10 3 1 5 -100
100 6 14"""
        output = """War"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
