import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    print(input().replace(",", " "))


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
        input = """happy,newyear,enjoy"""
        output = """happy newyear enjoy"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """haiku,atcoder,tasks"""
        output = """haiku atcoder tasks"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """abcde,fghihgf,edcba"""
        output = """abcde fghihgf edcba"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
