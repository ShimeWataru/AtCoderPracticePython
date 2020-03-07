import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, a, b = map(int, input().split())
    l = [list(input().split()) for i in range(n)]
    ans = 0
    for i in range(n):
        d = 0
        if int(l[i][1]) < a:
            d = a
        elif int(l[i][1]) > b:
            d = b
        else:
            d = int(l[i][1])
        if l[i][0] == "West":
            ans -= d
        else:
            ans += d

    if ans > 0:
        print("East", ans)
    elif ans < 0:
        print("West", abs(ans))
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

    def test_input1(self):
        print("test_input1")
        input = """3 5 10
East 7
West 3
West 11"""
        output = """West 8"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """3 3 8
West 6
East 3
East 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """5 25 25
East 1
East 1
West 1
East 100
West 1"""
        output = """East 25"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
