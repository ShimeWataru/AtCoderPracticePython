import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    n = int(input())
    l = [list(input().split()) for i in range(n)]
    start = []
    end = []
    d = True
    for i in range(n):
        if l[i][0] == "1":
            d = not (d)
        else:
            if l[i][1] == "1":
                if d:
                    start.append(l[i][2])
                else:
                    end.append(l[i][2])
            else:
                if d:
                    end.append(l[i][2])
                else:
                    start.append(l[i][2])
    if d:
        print("".join(start[::-1]) + s + "".join(end))
    else:
        print("".join(end[::-1]) +
              ''.join(list(reversed(s))) + "".join(start))


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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
