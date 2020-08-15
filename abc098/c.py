import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    l = [0] * n
    r = [0] * n
    ans = n
    for i in range(n):
        if i == 0:
            if s[0] == "W":
                l[0] = 1
        elif s[i] == "W":
            l[i] = l[i - 1] + 1
        else:
            l[i] = l[i - 1]
        if i == 0:
            if s[-1] == "E":
                r[0] = 1
        elif s[-i-1] == "E":
            r[i] = r[i - 1] + 1
        else:
            r[i] = r[i - 1]
    for i in range(n):
        if i == 0:
            ans = min(ans, r[n - 1 - i])
        elif i == n - 1:
            ans = min(ans, l[i - 1])
        else:
            ans = min(ans, l[i - 1] + r[n - 1 - i])
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
        input = """5
WEEWW"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()