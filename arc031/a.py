import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    check = True
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            check = False
            break
    print("YES" if check else "NO")

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
        input = """awawa"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """chokudai"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()