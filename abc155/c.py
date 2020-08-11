import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = {}
    for i in range(n):
        s = input()
        if s in a:
            a[s] += 1
        else:
            a[s] = 1
    a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    max_a = a[0][1]
    w = []
    for i in range(len(a)):
        if a[i][1] == max_a:
            w.append(a[i][0])
        else:
            break
    w = sorted(w)
    for i in range(len(w)):
        print(w[i])


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
        input = """7
beat
vet
beet
bed
vet
bet
beet"""
        output = """beet
vet"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo"""
        output = """buffalo"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """7
bass
bass
kick
kick
bass
kick
kick"""
        output = """kick"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """4
ushi
tapu
nichia
kun"""
        output = """kun
nichia
tapu
ushi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
