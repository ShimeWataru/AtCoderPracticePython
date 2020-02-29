import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = int(input())
    b = int(input())
    ans = 1
    for _ in range(a):
        if ans < b:
            ans *= 2
        else:
            ans += b
    print(ans)


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
        input = """4
3"""
        output = """10"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10
10"""
        output = """76"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
