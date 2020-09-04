import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    l = list(input()[:-1].split())
    ans = 0
    ans += l.count("TAKAHASHIKUN")
    ans += l.count("Takahashikun")
    ans += l.count("takahashikun")
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
        input = """5
Takahashikun is not an eel."""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
TAKAHASHIKUN loves TAKAHASHIKUN and takahashikun."""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
He is not takahasikun but Takahashikun."""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1
takahashikunTAKAHASHIKUNtakahashikun."""
        output = """0"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """18
You should give Kabayaki to Takahashikun on July twenty seventh if you suspect that he is an eel."""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()