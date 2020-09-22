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
    n = int(input())
    print("WANWAN" if is_prime(n * (n + 1) / 2) else "BOWWOW")

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
        input = """2"""
        output = """WANWAN"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """5"""
        output = """BOWWOW"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """1"""
        output = """BOWWOW"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """999"""
        output = """BOWWOW"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()