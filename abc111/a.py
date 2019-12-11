import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    print(input().replace("1", "3").replace("9", "1").replace("3", "9"))


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
        input = """119"""
        output = """991"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """999"""
        output = """111"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
