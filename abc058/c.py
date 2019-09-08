import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, n = map(int, input().split())
    b = list(map(str, input().split()))
    c = str(a)
    while True:
        check = True
        for i in range(len(c)):
            if c[i] in b:
                c = str(int(c) + 1)
                check = False
                break
        if check:
            print(c)
            break


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
        input = """1000 8
1 3 4 5 6 7 8 9"""
        output = """2000"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9999 1
0"""
        output = """9999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
