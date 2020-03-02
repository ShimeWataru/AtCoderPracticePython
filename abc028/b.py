import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    l = 'ABCDEF'
    ans = ""
    for i in range(6):
        ans += str(s.count(l[i]))
        if i == 5:
            print(ans)
        else:
            ans += " "


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """BEAF"""
        output = """1 1 0 0 1 1"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """DECADE"""
        output = """1 0 1 2 2 0"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """ABBCCCDDDDEEEEEFFFFFF"""
        output = """1 2 3 4 5 6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
