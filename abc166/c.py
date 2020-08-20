import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    h.insert(0,0)
    l = [list(map(int, input().split())) for i in range(m)]
    d = [[] for i in range(len(h))]
    ans = 0
    for i in range(1, n + 1):
        d[i].append(h[i])
    print(h)
    print(l)
    for i in range(m):
        d[l[i][0]].append(h[l[i][1]])
        d[l[i][1]].append(h[l[i][0]])
    print(d)
    for i in range(1, n + 1):
        if d[i][0] == max(d[i]):
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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()