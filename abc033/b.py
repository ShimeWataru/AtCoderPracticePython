import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    m = int(input())
    l = [list(input().split()) for i in range(m)]
    sum_l = 0
    max_l = 0
    max_i = 0
    for i in range(m):
        sum_l += int(l[i][1])
        if max_l < int(l[i][1]):
            max_l = int(l[i][1])
            max_i = i
    if max_l > sum_l // 2:
        print(l[max_i][0])
    else:
        print("atcoder")


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
        input = """4
unagi 20
usagi 13
snuke 42
smeke 7"""
        output = """snuke"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
a 10
b 20
c 30
d 40
e 100"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """14
yasuzuka 3340
uragawara 4032
oshima 2249
maki 2614
kakizaki 11484
ogata 10401
kubiki 9746
yoshikawa 5142
joetsu 100000
nakago 4733
itakura 7517
kiyosato 3152
sanwa 6190
nadachi 3169"""
        output = """joetsu"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
