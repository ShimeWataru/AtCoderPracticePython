import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    ans = ""
    for i in range(len(s)):
        if i % 2 == 0:
            ans += s[i]
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
        input = """atcoder"""
        output = """acdr"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """aaaa"""
        output = """aa"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """z"""
        output = """z"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """fukuokayamaguchi"""
        output = """fkoaaauh"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
