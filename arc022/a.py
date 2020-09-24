import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
import re
def resolve():
    check = re.search("^(.)*I(.)*C(.)*T(.)*$", input().upper())
    print("YES" if check else "NO")

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
        input = """InformationAndCommunicationTechnology"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """InformationTechnology"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """SinCosTan"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """Ticket"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input5(self):
        print("test_input5")
        input = """InternetTrouble"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()