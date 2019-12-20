import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    ans = 0
    for j in range(n + 1):
        ass = []
        for i in range(1, int(j**0.5)+1):
            if j % i == 0:
                ass.append(i)
                if i**2 == j:
                    continue
                ass.append(j//i)
        if j % 2 == 1 and len(ass) == 8:
            ans += 1
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
        input = """105"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """7"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
