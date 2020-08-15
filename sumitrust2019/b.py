import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    tmp = n // 1.08
    if tmp * 1.08 // 1 == n:
        print(int(tmp//1))
    elif (tmp + 1) * 1.08 // 1 == n:
        print(int((tmp + 1)//1))
    else:
        print(":(")

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
        input = """432"""
        output = """400"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1079"""
        output = """:("""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1001"""
        output = """927"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()