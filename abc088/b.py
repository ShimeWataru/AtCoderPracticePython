import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    List = list(map(int, input().split()))
    List = sorted(List)[::-1]
    alice = sum(List[0::2])
    bob = sum(List[1::2])
    print(alice - bob)


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
        input = """2
3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
2 7 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4
20 18 2 18"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
