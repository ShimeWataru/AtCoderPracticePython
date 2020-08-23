import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, k = map(int, input().split())
    for i in range(k):
        if i % 2 == 0:
            if a % 2 == 1:
                a -= 1
            b += a// 2
            a //= 2
        else:
            if b % 2 == 1:
                b -= 1
            a += b// 2
            b //= 2

    print(a,b)

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
        input = """5 4 2"""
        output = """5 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 3"""
        output = """1 3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """314159265 358979323 84"""
        output = """448759046 224379523"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()