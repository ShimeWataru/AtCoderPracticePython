import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    s = input()
    check = True
    for i in range(len(s)):
        if i == 0:
            if not (s[i] == "A"):
                check = False
        elif i == 2:
            if not (s[i] == "C"):
                check = False
        else:
            if not(s[i].islower()):
                check = False
    if check:
        print("AC")
    else:
        print("WA")


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
        input = """AtCoder"""
        output = """AC"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """ACoder"""
        output = """WA"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """AcycliC"""
        output = """WA"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """AtCoCo"""
        output = """WA"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """Atcoder"""
        output = """WA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
