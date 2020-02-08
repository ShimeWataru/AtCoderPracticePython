import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = input()
    b = input()
    c = input()
    print(a[0]+b[1]+c[2])


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
        input = """ant
obe
rec"""
        output = """abc"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """edu
cat
ion"""
        output = """ean"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
