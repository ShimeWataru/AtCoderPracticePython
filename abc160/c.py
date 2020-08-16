import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k, n = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0] * n
    for i in range(n):
        if i == n - 1:
            d[i] = k - l[-1] + l[0]
        else:
            d[i] = l[i + 1] - l[i]
    print(k - max(d))

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
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()