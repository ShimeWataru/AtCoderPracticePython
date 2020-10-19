import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l = list(map(int,input().split()))
    check = False

    for i in range(2 ** 4):
        sum_1 = 0
        sum_2 = 0
        for j in range(4):
            if ((i >> j) & 1):
                sum_1 += l[j]
            else:
                sum_2 += l[j]
        if sum_1 == sum_2:
            check = True
    print("Yes" if check else "No")

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
        input = """1 3 2 4"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()