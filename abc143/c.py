import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    s = input()
    c = [0] * len(s)
    o = s[0]
    ans = []
    for i in range(1, len(s)):
        if s[i] == o:
            c[i] = 1
        else:
            o = s[i]

    for i in range(len(s)):
        if c[i] == 0:
            ans.append(s[i])
    print(len("".join(ans)))


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
        input = """10
aabbbbaaca"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
aaaaa"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """20
xxzaffeeeeddfkkkkllq"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
