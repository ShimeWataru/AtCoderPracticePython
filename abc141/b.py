import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a = input()
    b = True
    for i in range(len(a)):
        if i % 2 == 0:
            if a[i] == 'R' or a[i] == 'U' or a[i] == 'D':
                continue
            else:
                b = False
                break
        else:
            if a[i] == 'L' or a[i] == 'U' or a[i] == 'D':
                continue
            else:
                b = False
                break
    if b:
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
        input = """RUDLUDR"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """DULL"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """UUUUUUUUUUUUUUU"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """ULURU"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """RDULULDURURLRDULRLR"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
