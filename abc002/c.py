import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    ax, ay, bx, by, cx, cy = map(int, input().split())
    bx = bx - ax
    by = by - ay
    cx = cx - ax
    cy = cy - ay
    ans = abs((bx * cy) - (by * cx)) / 2
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
        input = """1 0 3 0 2 5"""
        output = """5.0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """-1 -2 3 4 5 6"""
        output = """2.0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """298 520 903 520 4 663"""
        output = """43257.5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()