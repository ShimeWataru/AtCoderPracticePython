import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m, a, b = map(int, input().split())
    l = [int(input()) for i in range(m)]
    check = True
    day = 0
    for i in range(m):
        if n <= a:
            n += b
        n -= l[i]
        if n < 0:
            check = False
            day = i + 1
            break
    print("complete" if check else day)
        

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
        input = """100 3 0 100
10
20
30"""
        output = """complete"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100 4 0 100
10
20
30
40"""
        output = """complete"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 4 0 100
50
40
30
20"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100 4 10 100
50
40
30
20"""
        output = """complete"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """5 3 20 10
15
5
20"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()