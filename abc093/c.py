import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, c = sorted(map(int, input().split()))
    ans = 0
    if (b - a) % 2 == 0:
        ans += ((b - a) // 2)
    else:
        b += 1
        c += 1
        ans += 1
        ans += ((b - a) // 2)
    ans += (c - b)
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
        input = """2 5 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 6 3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """31 41 5"""
        output = """23"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()