import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, a, b = map(int, input().split())
    while (n > 0):
        n -= a
        if n <= 0:
            print("Ant")
            break
        n -= b
        if n <= 0:
            print("Bug")
            break

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
        input = """5 1 2"""
        output = """Bug"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """10 3 4"""
        output = """Ant"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()