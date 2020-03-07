import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = list(map(int, input().split()))
    l = sorted(l)
    print(l[0] if not l[0] == l[1] else l[2])


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
        input = """1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """4 3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """5 5 5"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
