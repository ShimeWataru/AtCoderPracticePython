import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    s = input()
    check = True
    if len(s) == a + b + 1:
        for i in range(len(s)):
            if i == a:
                if not (s[i] == '-'):
                    check = False
            else:
                if not (s[i] in '0123456789'):
                    check = False
    else:
        check = False
    if check:
        print("Yes")
    else:
        print("No")


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
        input = """3 4
269-6650"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1 1
---"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 2
7444"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
