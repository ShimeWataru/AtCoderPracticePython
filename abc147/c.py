import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = []
    ans = 0
    check = True
    for _ in range(n):
        m = int(input())
        l.append([list(map(int, input().split())) for _ in range(m)])
    for i in range(2 ** n):
        bin_i = format(i, 'b').rjust(n, "0")
        for k in range(n):
            check = True
            for x in range(len(l[k])):
                if bin_i[k] == "1":
                    if (bin_i[l[k][x][0] - 1] == "1") and (l[k][x][1] == 0):
                        check = False
                    elif (bin_i[l[k][x][0]-1] == "0") and (l[k][x][1] == 1):
                        check = False
        if check:
            ans = max(ans, bin_i.count("1"))
            print(bin_i)
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
        input = """3
1
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
