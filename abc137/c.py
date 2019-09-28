import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    N = int(input())
    dic = {}
    for i in range(N):
        s = list(input())
        s.sort()
        key = str(s)
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1

    ans = 0
    for value in dic.values():
        ans += value*(value-1) / 2
    print(int(ans))


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
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
