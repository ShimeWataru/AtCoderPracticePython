import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = [int(input()) for i in range(3)]
    s = sorted(a)[::-1]
    for i in range(3):
        for j in range(3):
            if a[i] == s[j]:
                print(j + 1)


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
        input = """12
18
11"""
        output = """2
1
3"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """10
20
30"""
        output = """3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
