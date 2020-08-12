import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = [input() for i in range(n)]
    print("AC x", l.count("AC"))
    print("WA x", l.count("WA"))
    print("TLE x", l.count("TLE"))
    print("RE x", l.count("RE"))

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
        input = """6
AC
TLE
AC
AC
WA
TLE"""
        output = """AC x 3
WA x 1
TLE x 2
RE x 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
AC
AC
AC
AC
AC
AC
AC
AC
AC
AC"""
        output = """AC x 10
WA x 0
TLE x 0
RE x 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()