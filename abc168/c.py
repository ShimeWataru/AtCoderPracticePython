import sys
from io import StringIO
import unittest
import logging
import math
logging.basicConfig(level=logging.DEBUG)

def resolve():
        a, b, h, m = map(int, input().split())
        ax = a * math.cos(math.radians((h/12 + 1/12 * m/60) * 360))
        ay = a * math.sin(math.radians((h/12 + 1/12 * m/60) * 360))
        bx = b * math.cos(math.radians(m/60 * 360))
        by = b * math.sin(math.radians(m/60 * 360))
        print(math.sqrt((ax-bx)**2 + (ay-by)**2))

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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()