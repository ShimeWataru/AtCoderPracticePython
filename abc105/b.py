import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    flg = False
    for i in range(26):
        for j in range(15):
            if i * 4 + j * 7 == n:
                flg = True
    if flg:
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
        input = """11"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """40"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
