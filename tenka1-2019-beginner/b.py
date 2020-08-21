import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    a = int(input())
    ans = ""
    for i in range(n):
        if s[i] == s[a - 1]:
            ans += s[i]
        else:
            ans += "*"
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
error
2"""
        output = """*rr*r"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
eleven
5"""
        output = """e*e*e*"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9
education
7"""
        output = """******i**"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()