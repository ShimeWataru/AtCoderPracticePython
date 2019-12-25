import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = []
    if n == 1:
        print(1)
    else:
        for i in range(1, n + 1):
            for j in range(2, n + 1):
                if i ** j > n:
                    break
                l.append(i ** j)
        l = list(set(l))
        l = sorted(l)
        ans = 0
        for i in range(len(l)):
            if l[i] > n:
                break
            ans = l[i]
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
        input = """10"""
        output = """9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """999"""
        output = """961"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
