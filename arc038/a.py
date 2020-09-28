import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)[::-1]
    ans = 0
    for i in range((-(-n // 2))):
        ans += l[i * 2]
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
    def test_input1(self):
        print("test_input1")
        input = """2
400 628"""
        output = """628"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """5
2 5 9 6 5"""
        output = """16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()