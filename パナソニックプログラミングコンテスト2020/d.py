import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


def resolve():
    n = int(input())
    ans = [[] for i in range(n)]
    ans[0].append("a")
    print(ans)
    b = 1
    for i in range(1, 10):
        for j in range(i ** i):
            print(j)
            # print(Base_10_to_n(j, i + 1))

            # ans[b].append


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
        input = """1"""
        output = """a"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """aa
ab"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
