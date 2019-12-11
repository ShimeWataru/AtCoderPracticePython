import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    l.append(0)
    adjustment = [0] * n
    base_money = 0
    position = 0
    for i in range(n):
        if position > l[i] and l[i] < l[i+1]:
            if position < l[i+1]:
                adjustment[i] = (abs(l[i + 1] - l[i]) -
                                 abs(l[i + 1] - position)) * 2
            else:
                adjustment[i] = (abs(l[i] - position) -
                                 abs(l[i + 1] - position)) * 2
        elif position < l[i] and l[i] > l[i + 1]:
            if position < l[i+1]:
                adjustment[i] = (abs(l[i] - position) -
                                 abs(l[i + 1] - position)) * 2
            else:
                adjustment[i] = (abs(l[i + 1] - l[i]) -
                                 abs(l[i + 1] - position)) * 2
        base_money += abs(l[i] - position)
        position = l[i]
    base_money += abs(position)
    for i in range(n):
        print(base_money - adjustment[i])


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
        input = """3
3 5 -1"""
        output = """12
8
10"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
1 1 1 2 0"""
        output = """4
4
4
2
4"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6
-679 -2409 -3258 3095 -3291 -4462"""
        output = """21630
21630
19932
8924
21630
19288"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
