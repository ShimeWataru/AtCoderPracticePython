import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    tmp_a = int((a / 0.08) // 1)
    tmp_b = int((b / 0.10) // 1)
    check = True
    # print(tmp_a, tmp_b)
    for i in range(min(tmp_a,tmp_b), max(tmp_a + 1, tmp_b + 1) + 1):
        if int((i * 0.08)//1) == a and int((i * 0.10)//1) == b:
            print(i)
            check = False
            break
    if check:
        print(-1)


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
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """25 32"""
        output = """320"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_4")
        input = """1 1"""
        output = """13"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()