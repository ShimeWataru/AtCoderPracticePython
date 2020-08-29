import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    a, b = map(int, input().split())
    l = list(map(int, input().split()))
    x = 0
    y = 0
    z = 0
    for i in range(n):
        if l[i] <= a:
            x += 1
        elif a + 1 <= l[i] <= b:
            y += 1
        elif b + 1 <= l[i]:
            z += 1
    print(min(x,y,z))

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
        input = """7
5 15
1 10 16 2 7 20 12"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8
3 8
5 5 5 10 10 10 15 20"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
5 6
5 6 10"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()