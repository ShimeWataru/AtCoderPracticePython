import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    t = input()
    match_s = 0
    for i in range(len(s) - len(t) + 1):
        tmp_match_s = 0
        for j in range(len(t)):
            if s[i + j] == t[j]:
                tmp_match_s += 1
        match_s = max(match_s, tmp_match_s)
    print(len(t)- match_s)

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
        input = """cabacc
abc"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """codeforces
atcoder"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()