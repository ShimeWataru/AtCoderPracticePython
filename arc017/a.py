import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def resolve():
    print("YES" if is_prime(int(input())) else "NO")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input１(self):
        print("test_input１")
        input = """17"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input２(self):
        print("test_input２")
        input = """18"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input３(self):
        print("test_input３")
        input = """999983"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input４(self):
        print("test_input４")
        input = """672263"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()