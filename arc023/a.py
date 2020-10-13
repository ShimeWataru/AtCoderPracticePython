import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    y = int(input())
    m = int(input())
    d = int(input())
    if m <= 2:
        m += 12
        y -= 1
    print(735369 - (365 * y + (y//4) - (y//100) + (y//400) + ((306 * (m+1))//10) + d - 429))

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
        input = """1988
7
3"""
        output = """9449"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1
1
1"""
        output = """735369"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """2014
5
16"""
        output = """1"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """2012
2
29"""
        output = """808"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()