import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    a = {}
    b = {}
    for i in range(n // 2):
        key_a = l[i * 2]
        key_b = l[i * 2 + 1]
        if key_a in a:
            a[key_a] = a[key_a] + 1
        else:
            a[l[i * 2]] = 1
        if key_b in b:
            b[key_b] = b[key_b] + 1
        else:
            b[key_b] = 1

    sorted(a.items(), key=lambda x: x[1], reverse=True)
    sorted(b.items(), key=lambda x: x[1], reverse=True)

    a = list(a.items())
    b = list(b.items())
    ca_max = a[0]
    cb_max = b[0]
    ca_max_num = a[0][1]
    cb_max_num = b[0][1]
    if ca_max[0] == cb_max[0]:
        if ca_max[1] > cb_max[1]:
            if len(b) > 1:
                cb_max_num = b[1][1]
            else:
                cb_max_num = 0
        else:
            if len(a) > 1:
                ca_max_num = a[1][1]
            else:
                ca_max_num = 0
    print((n // 2) * 2 - ca_max_num - cb_max_num)


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
3 1 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """6
105 119 105 119 105 119"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4
1 1 1 1"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
