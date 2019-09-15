import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = list(map(int, input().split()))
    while (len(b) > 1):
        b = sorted(b)
        x = b.pop(0)
        y = b.pop(0)
        b.append((x+y)/2)
    print(b[0])
    pass


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
3 4"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
500 300 200"""
        output = """375"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
138 138 138 138 138"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
