import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    ans = {}
    n = int(input())
    l = [input() for i in range(n)]
    for i in range(n):
        if l[i] in ans:
            ans[l[i]] = ans[l[i]] + 1
        else:
            ans[l[i]] = 1
    ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    print(ans[0][0])


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
        input = """4
taro
jiro
taro
saburo"""
        output = """taro"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """1
takahashikun"""
        output = """takahashikun"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """9
a
b
c
c
b
c
b
d
e"""
        output = """b"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
