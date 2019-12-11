import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    for i in range(n, 1000):
        s = str(i)
        if s[0] == s[1] == s[2]:
            print(i)
            break


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
        input = """111"""
        output = """111"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """112"""
        output = """222"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """750"""
        output = """777"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
