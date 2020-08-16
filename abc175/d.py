import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    p = list(map(int,input().split()))
    c = list(map(int, input().split()))
    pt = [0] * n
    pt_round = sum(c)
    for i in range(n):
        pt_tmp = 0
        pt_tmp_max = -100000000000
        now = i
        for j in range(max(k % n, n)):
            pt_tmp += c[p[now] - 1]
            now = p[now] - 1
            pt_tmp_max = max(pt_tmp, pt_tmp_max)
        pt[i] = pt_tmp_max
    if pt_round > 0:
        print((k // n) * pt_round + max(pt))
    else:
        print(max(pt))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
#     def test_input_1(self):
#         print("test_input_1")
#         input = """5 2
# 2 4 5 1 3
# 3 4 -10 -8 8"""
#         output = """8"""
#         self.assertIO(input, output)
#     def test_input_2(self):
#         print("test_input_2")
#         input = """2 3
# 2 1
# 10 -7"""
#         output = """13"""
#         self.assertIO(input, output)
#     def test_input_3(self):
#         print("test_input_3")
#         input = """3 3
# 3 1 2
# -1000 -2000 -3000"""
#         output = """-1000"""
#         self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719"""
        output = """29507023469"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()