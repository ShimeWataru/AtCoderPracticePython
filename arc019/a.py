import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    s = s.replace('O','0')
    s = s.replace('D','0')
    s = s.replace('I','1')
    s = s.replace('Z','2')
    s = s.replace('S','5')
    s = s.replace('B', '8')
    print(s)

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
        input = """1Z0"""
        output = """120"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """4ZD6O"""
        output = """42060"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """BI9Z"""
        output = """8192"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()