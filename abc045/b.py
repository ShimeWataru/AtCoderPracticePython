import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = list(input())
    b = list(input())
    c = list(input())
    next = 'a'
    target = a
    while(True):
        if next == 'a':
            target = a
        elif next == 'b':
            target = b
        else:
            target = c
        if len(target) == 0:
            print(next.upper())
            break
        next = target[0]
        target.pop(0)


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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
