import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [input() for i in range(n)]
    last = l[0][-1]
    old = [l[0]]
    check = True
    for i in range(1, n):
        if l[i][0] != last or l[i] in old:
            check = False
        else:
            old.append(l[i])
            last = l[i][-1]
    if check:
        print("Yes")
    else:
        print("No")


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
hoge
english
hoge
enigma"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """9
basic
c
cpp
php
python
nadesico
ocaml
lua
assembly"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """3
abc
arc
agc"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
