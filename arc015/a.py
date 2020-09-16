import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    print(9 / 5 * int(input()) + 32)

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
        input = """10"""
        output = """50"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """33"""
        output = """91.4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """-100"""
        output = """-148"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()