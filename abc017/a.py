import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    l = [list(map(int, input().split())) for i in range(3)]
    ans = 0
    for i in range(3):
        ans += l[i][0] * l[i][1] // 10
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

    def test_input1(self):
        print("test_input1")
        input = """50 7
40 8
30 9"""
        output = """94"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """990 10
990 10
990 10"""
        output = """2970"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
