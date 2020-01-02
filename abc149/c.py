import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def segment_sieve(a, b):
    ass = []
    is_prime_small = [True] * (int(b**0.5)+1)
    is_prime = [True] * (b-a)
    for i in range(2, int(b**0.5)):
        if is_prime_small[i]:
            j = 2*i
            while j**2 < b:
                is_prime_small[j] = False
                j += i
            j = max(2*i, ((a+i-1)//i)*i)
            while j < b:
                is_prime[j-a] = False
                j += i
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(a + i)
            return ass
    if ass[0] == 1:
        del ass[0]
    return ass


def resolve():
    x = int(input())
    print(segment_sieve(x, 100004)[0])


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
        input = """20"""
        output = """23"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """99992"""
        output = """100003"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
