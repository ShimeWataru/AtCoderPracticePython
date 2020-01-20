import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    map_ans = []
    ans = 0
    for i in range(10):
        map_ans.append([0] * 10)
    for i in range(1, n + 1):
        pre = str(i)[0]
        suf = str(i)[-1]
        map_ans[int(pre)][int(suf)] += 1
    for i in range(1, 10):
        for j in range(1, 10):
            ans += map_ans[i][j] * map_ans[j][i]
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
        input = """25"""
        output = """17"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """100"""
        output = """108"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """2020"""
        output = """40812"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_5")
        input = """200000"""
        output = """400000008"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
