import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    check = True
    for i in range(n):
        if l[i] % 2 == 1:
            next
        else:
            if l[i] % 3 == 0 or l[i] % 5 == 0:
                next
            else:
                check = False
    if check:
        print("APPROVED")
    else:
        print("DENIED")


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
        input = """5
6 7 9 10 31"""
        output = """APPROVED"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
28 27 24"""
        output = """DENIED"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
