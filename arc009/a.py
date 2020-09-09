import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += a * b
    print(int(ans * 1.05 //1))


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
        input = """2
4 120
2 130"""
        output = """777"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
1 100"""
        output = """105"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
3 510
1 835
2 140
6 205"""
        output = """4068"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10
8 10
7 189
4 545
1 596
3 209
10 850
9 943
6 921
8 984
10 702"""
        output = """44321"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()