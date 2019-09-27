import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = input()
    l = list(map(int, input().split()))

    s = 0
    now = l[0]
    count = 0
    for i in range(1, len(l)):
        if s == 0:
            if l[i] > now:
                s = 1
            elif l[i] < now:
                s = -1
        elif s == 1:
            if not (l[i] >= now):
                count += 1
                s = 0
        else:
            if l[i] > now:
                count += 1
                s = 0
        now = l[i]
    print(count + 1)


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
1 2 3 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9
1 2 1 2 1 2 1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """7
1 2 3 2 1 999999999 1000000000"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
