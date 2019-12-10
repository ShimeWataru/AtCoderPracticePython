import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = int(input())
    l = [s]
    for i in range(1, 1000001):
        num_i = 1000001
        if l[i - 1] % 2 == 0:
            num_i = l[i - 1] / 2
        else:
            num_i = l[i - 1] * 3 + 1
        if num_i in l:
            print(i+1)
            break
        else:
            l.append(num_i)


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
        input = """8"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """7"""
        output = """18"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """54"""
        output = """114"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
