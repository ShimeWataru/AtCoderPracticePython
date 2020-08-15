import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l = list(map(int, input().split()))
    ans = []
    for i in range(len(l)-2):
        for j in range(i + 1, len(l)-1):
            for k in range(j + 1, len(l)):
                ans.append(l[i] + l[j] + l[k])
    ans = sorted(set(ans), reverse=True)
    print(ans[2])


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
        input = """1 2 3 4 5"""
        output = """10"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1 2 3 5 8"""
        output = """14"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()