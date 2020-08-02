import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    n = n % 10
    if n in [2, 4, 5, 7, 9]:
      print("hon")
    elif n in [0,1,6,8]:
      print("pon")
    else:
      print("bon")

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
        input = """16"""
        output = """pon"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """hon"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """183"""
        output = """bon"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()