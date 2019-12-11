import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        des = 0
        if l[i] + l[i - 1] > x:
            des = (l[i] + l[i - 1]) - x
            if l[i] >= des:
                l[i] -= des
            else:
                l[i] = 0
                l[i - 1] -= (des - l[i])
        ans += des
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
        input = """3 3
2 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6 1
1 6 1 2 0 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 9
3 1 4 1 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """2 0
5 5"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
