import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, x, y = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        if l[i][0] >= x and l[i][1] >= y:
            ans += 1
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
        input = """3 5 2
10 3
5 2
2 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 587586158 185430194
894597290 708587790
680395892 306946994
590262034 785368612
922328576 106880540
847058850 326169610
936315062 193149191
702035777 223363392
11672949 146832978
779291680 334178158
615808191 701464268"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()