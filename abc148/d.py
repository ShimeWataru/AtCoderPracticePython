import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    num = 1
    old_i = 0
    for i in range(n):
        if l[i] == num:
            # print(i, num, ans, (i - old_i))
            ans += (i - old_i)
            old_i = i + 1
            num += 1
    ans += (i - old_i + 1)
    if num == 1:
        print(-1)
    else:
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
2 1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
2 2 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """1
1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """6
2 1 2 4 3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_6(self):
        print("test_input_6")
        input = """4
2 1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_7(self):
        print("test_input_7")
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_8(self):
        print("test_input_8")
        input = """5
5 4 3 2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_9(self):
        print("test_input_9")
        input = """5
1 1 1 1 1"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
