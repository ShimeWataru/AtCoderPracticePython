import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    dis = 0
    ans = 0
    if sum(l) <= x:
        print(len(l) + 1)
    else:
        while (dis <= x):
            dis += l[ans]
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
        input = """3 6
3 4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 9
3 3 3 3"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
