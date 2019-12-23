import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = input()
    s = input()
    ans = 0
    tmp = 0
    old = []
    for i in range(1, len(s)):
        tmp = 0
        old = []
        for j in range(i):
            if s[j] in s[i:] and not(s[j] in old):
                tmp += 1
                old.append(s[j])
        ans = max(ans, tmp)
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
        input = """6
aabbca"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
