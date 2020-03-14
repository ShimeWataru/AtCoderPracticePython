import collections
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    N, Q = map(int, input().split())
    count = [0] * (N + 1)
    g = [[] for _ in range(N+1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for _ in range(Q):
        v, val = map(int, input().split())
        count[v] += val
    q = collections.deque()
    q.append(1)
    check = [0] * (N + 1)
    while q:
        v = q.pop()
        check[v] = 1
        for u in g[v]:
            if check[u] == 1:
                continue
            count[u] += count[v]
            q.append(u)
    print(*count[1:])


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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
