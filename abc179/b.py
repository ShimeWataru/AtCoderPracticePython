import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = [list(map(int, input().split())) for i in range(n)]
    max_cnt = 0
    now_cnt = 0
    for i in range(n):
        if len(set(l[i])) == 1:
            now_cnt += 1
            max_cnt = max(max_cnt, now_cnt)
        else:
            now_cnt = 0
    print("Yes" if max_cnt >= 3 else "No")

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
1 2
6 6
4 4
3 3
3 2"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 1
2 2
3 4
5 5
6 6"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
1 1
2 2
3 3
4 4
5 5
6 6"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()