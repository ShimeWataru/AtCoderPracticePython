import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    c = [0] * (a+1)
    for i in range(b):
        x, y = map(int, input().split())
        c[x] += 1
        c[y] += 1
    for j in range(1, len(c)):
        print(c[j])


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
        input = """4 3
1 2
2 3
1 4"""
        output = """2
2
1
1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 5
1 2
2 1
1 2
2 1
1 2"""
        output = """5
5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8 8
1 2
3 4
1 5
2 8
3 7
5 2
4 1
6 8"""
        output = """3
3
2
2
2
1
1
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
