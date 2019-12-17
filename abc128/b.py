import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [list(input().split()) for _ in range(n)]
    for i in range(n):
        l[i].append(i + 1)
    l = sorted(
        l,
        key=lambda x: (x[0], -int(x[1]))
    )
    for i in range(n):
        print(l[i][2])


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
        input = """6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40"""
        output = """3
4
6
1
5
2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10
yakutsk 10
yakutsk 20
yakutsk 30
yakutsk 40
yakutsk 50
yakutsk 60
yakutsk 70
yakutsk 80
yakutsk 90
yakutsk 100"""
        output = """10
9
8
7
6
5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
