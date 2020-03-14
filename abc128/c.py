import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    # n, m = map(int, input().split())
    # l = [list(map(int, input().split())) for _ in range(m)]
    # p = list(map(int, input().split()))
    # count = 0
    # for i in range(2 ** n):
    #     check = True
    #     bin_str = format(i, 'b').rjust(n + 1, "0")
    #     for j in range(m):
    #         light = 0
    #         for k in range(1, len(l[j])):
    #             if bin_str[l[j][k]] == "1":
    #                 light += 1
    #         if not (light % 2 == p[j]):
    #             check = False
    #     if check:
    #         count += 1
    # print(count)
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(m)]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** n):
        check = True
        for j in range(m):
            light = 0
            for k in range(1, len(l[j])):
                if ((i >> l[j][k] - 1) & 1):
                    light += 1
            if light % 2 != p[j]:
                check = False
        if check:
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
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
