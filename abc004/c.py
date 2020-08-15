import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = ["1", "2", "3", "4", "5", "6"]
    for i in range(n % 30):
        a = i % 5
        b = a + 1
        l[a], l[b] = l[b], l[a]
    print(''.join(l))


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
        input = """1"""
        output = """213456"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5"""
        output = """234561"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """22"""
        output = """615234"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100000000"""
        output = """345612"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()