import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    t = int(input())
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    c_a = 0
    check = True

    for i in range(m):
        if n - c_a < m - i:
            check = False
            break
        for j in range(c_a, n):
            if a[j] <= b[i] <= a[j] + t:
                c_a = j + 1
                break
            elif j == n - 1:
                check = False
                break
    print("yes" if check else "no")


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
        input = """1
3
1 2 3
3
2 3 4"""
        output = """yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
3
1 2 3
3
2 3 5"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
3
1 2 3
10
1 2 3 4 5 6 7 8 9 10"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1
3
1 2 3
3
1 2 2"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """2
5
1 3 6 10 15
3
4 8 16"""
        output = """yes"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()