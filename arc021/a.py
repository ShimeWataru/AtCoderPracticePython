import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l = [list(map(int, input().split())) for i in range(4)]
    check = False
    for i in range(3):
        for j in range(4):
            if l[i][j] == l[i + 1][j]:
                check = True
    for i in range(3):
        for j in range(4):
            if l[j][i] == l[j][i + 1]:
                check = True
    print("CONTINUE" if check else "GAMEOVER")

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
        input = """2 8 2 2
32 2 8 8
4 64 2 128
2 8 4 2"""
        output = """CONTINUE"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """2 4 16 4
8 32 128 8
2 64 16 2
32 4 32 4"""
        output = """GAMEOVER"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """2 4 2 4
4 2 4 2
2 4 2 4
4 2 4 2"""
        output = """GAMEOVER"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()