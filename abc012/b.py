import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    h = str(n//3600).rjust(2, '0')
    m = str((n % 3600)//60).rjust(2, '0')
    s = str(n % 60).rjust(2, '0')
    print("{}:{}:{}".format(h, m, s))


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
        input = """3661"""
        output = """01:01:01"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """86399"""
        output = """23:59:59"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
