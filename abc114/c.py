import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

l = []


def sft(n, num, add):
    int_sft = int(num+add)
    if int_sft > n:
        return True
    else:
        l.append(int_sft)
        sft(n, num+add, "3")
        sft(n, num+add, "5")
        sft(n, num+add, "7")


def resolve():
    n = int(input())
    sft(n, "", "3")
    sft(n, "", "5")
    sft(n, "", "7")
    le = []
    for i in range(len(l)):
        c3 = str(l[i]).count("3")
        c5 = str(l[i]).count("5")
        c7 = str(l[i]).count("7")
        if c3 > 0 and c5 > 0 and c7 > 0:
            le.append(l[i])
    print(len(list(set(le))))


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
        input = """575"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3600"""
        output = """13"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """999999999"""
        output = """26484"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
