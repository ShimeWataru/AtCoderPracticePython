import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    c = sorted(c)
    count = 0
    for i in range(a):
        b = b - c[i]
        if i == a - 1:
            if (b == 0):
                count += 1
        else:
            if (b >= 0):
                count += 1
            else:
                break
    print(count)


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
        input = """3 70
20 30 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 10
20 30 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4 1111
1 10 100 1000"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """2 10
20 20"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
