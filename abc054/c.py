import itertools
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(m)]
    r = [[] for i in range(n + 1)]
    ans = 0
    for i in range(m):
        r[l[i][0]].append(l[i][1])
        r[l[i][1]].append(l[i][0])
    p = "2345678"[:n-1]
    p = list(itertools.permutations(p))
    for i in range(len(p)):
        check = True
        t = "1" + "".join(p[i])
        for j in range(len(t)-1):
            if not int(t[j + 1]) in r[int(t[j])]:
                check = False
        if check:
            ans += 1
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
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
