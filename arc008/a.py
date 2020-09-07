import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    if n % 10 >= 7:
        print((-(-n // 10) * 100))
    else:
        print(n//10 * 100 + n % 10 * 15)

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
        input = """2"""
        output = """30"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5"""
        output = """75"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7"""
        output = """100"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()