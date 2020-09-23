import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    ans = "Bug"
    if abs(a) == abs(b):
        ans = "Draw"
    elif abs(a) < abs(b):
        ans = "Ant"
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
    def test_input1(self):
        print("test_input1")
        input = """2 3"""
        output = """Ant"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1 0"""
        output = """Bug"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """-100 100"""
        output = """Draw"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()