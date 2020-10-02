import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = [input() for i in range(n)]
    old = [l[0]]
    last = l[0][-1]
    check = False
    result = ""
    for i in range(1, n):
        if l[i][0] != last or l[i] in old:
            result = "WIN" if i % 2 != 0 else "LOSE"
            check = True
            break
        old.append(l[i])
        last = l[i][-1]
    print(result if check else "DRAW")

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
        input = """4
ab
ba
ab
cb"""
        output = """LOSE"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
atcoder
redcoder
recorder"""
        output = """DRAW"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()