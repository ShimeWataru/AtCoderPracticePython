import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, c = map(int, input().split())
    k = int(input())
    count = 0
    while (a >= b):
        b *= 2
        count += 1
    while (b >= c):
        c *= 2
        count += 1
    check = k >= count
    print("Yes" if check else "No")

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
        input = """7 2 5
3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 4 2
3"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()