import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    count = 0

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if 500 * i + 100 * j + 50 * k == x:
                    count += 1
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
        input = """2
2
2
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
1
0
150"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """30
40
50
6000"""
        output = """213"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
