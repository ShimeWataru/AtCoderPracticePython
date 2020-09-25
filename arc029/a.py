import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = [int(input()) for i in range(n)]
    if n <= 2:
        print(max(l))
    elif n == 3:
        print(max(max(l), sum(l) - max(l)))
    else:
        ans = 99999999
        for i in range(2 ** 4):
            a = []
            b = []
            for j in range(4):
                if ((i >> j) & 1):
                    a.append(l[j])
                else:
                    b.append(l[j])
            ans = min(ans, max(sum(a), sum(b)))
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
    def test_input1(self):
        print("test_input1")
        input = """4
4
6
7
10"""
        output = """14"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """3
1
2
4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """1
29"""
        output = """29"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()