import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = input()
    print(input().replace(x, ""))

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
        input = """a
abcdefgabcdefg"""
        output = """bcdefgbcdefg"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """g
aassddffgg"""
        output = """aassddff"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """a
aaaaa"""
        output = """"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """l
qwertyuiopasdfghjklzxcvbnm"""
        output = """qwertyuiopasdfghjkzxcvbnm"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """d
qwsdtgcszddddsdfgvbbnj"""
        output = """qwstgcszsfgvbbnj"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()