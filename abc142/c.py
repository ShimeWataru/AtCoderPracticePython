import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ll = []
    ans = []
    for i in range(len(l)):
        ll.append([i + 1, l[i]])
    ll = sorted(ll, key=lambda x: x[1])
    for i in range(len(l)):
        ans.append(str(ll[i][0]))
    print(' '.join(ans))


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
2 3 1"""
        output = """3 1 2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
1 2 3 4 5"""
        output = """1 2 3 4 5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8
8 2 7 3 4 5 6 1"""
        output = """8 2 4 5 6 7 3 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
