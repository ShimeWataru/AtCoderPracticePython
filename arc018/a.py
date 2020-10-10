import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h, b = map(float, input().split())
    print(b * (h/100) ** 2)

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
        input = """160.0 23.5"""
        output = """60.160"""
        self.assertIO(input, output)
    def test_input２(self):
        print("test_input２")
        input = """199.9 11.1"""
        output = """44.356"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()