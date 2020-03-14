import bisect
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def isok(x, k, a, b):
    cnt = 0
    for i in range(len(a)):
        cnt += bisect.bisect_right(b, x // a[i])
    return cnt >= k


def resolve():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    ok = 10 ** 18 + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = abs(ok + ng) // 2
        if isok(mid, k, a, b):
            ok = mid
        else:
            ng = mid
    print(ok)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """2 3
2 3
3 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """3 7
1 2 1
2 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """4 8
701687787 500872619 516391519 599949380
458299111 633119409 377269575 717229869"""
        output = """317112176525562171"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
