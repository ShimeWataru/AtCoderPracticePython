import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = [int(input()) for i in range(5)]
    min = 9
    min_index = 0
    sum = 0
    for i in range(len(l)):
        if l[i] % 10 != 0 and l[i] % 10 < min:
            min = l[i] % 10
            min_index = i
    for i in range(len(l)):
        if i != min_index:
            sum += (l[i] + 9) // 10 * 10
    sum += l[min_index]
    print(sum)


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
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
