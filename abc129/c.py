import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)]
    kaidan = [-1] * (n + 1)
    for i in range(len(l)):
        kaidan[l[i][0]] = 0
    for i in range(1, len(kaidan) + 1):
        if not (kaidan[-i] == 0):
            if i == 1:
                kaidan[-1] = 1
            elif i == 2:
                kaidan[-2] = kaidan[-1]
            else:
                kaidan[-i] = kaidan[-i + 1] + kaidan[-i + 2]
    print(kaidan[0] % 1000000007)


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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
