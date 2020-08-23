import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    max_l = 0
    ans = 0
    for i in range(n):
        if l[i] < max_l:
            ans += max_l - l[i]
        max_l = max(max_l, l[i])
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
        input = """5
2 1 5 4 3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
3 3 3 3 3"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()