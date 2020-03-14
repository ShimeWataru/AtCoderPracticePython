import collections
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    H, W = map(int, input().split())
    l = [input() for _ in range(H)]
    check = [([0] * (W)) for _ in range(H)]
    white = 0
    for i in range(H):
        white += l[i].count(".")
    q = collections.deque()
    check[0][0] = 1
    q.append([0, 0])
    g = False
    while q:
        h, w = q.popleft()
        for i, j in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            new_h = h + i
            new_w = w + j
            if new_w < 0 or new_h < 0 or new_w > W-1 or new_h > H-1 or l[new_h][new_w] == "#":
                continue
            elif check[new_h][new_w] == 0:
                check[new_h][new_w] = check[h][w] + 1
                q.append([new_h, new_w])
    print(white - check[H-1][W-1] if check[H-1][W-1] != 0 else -1)


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
        input = """3 3
..#
#..
..."""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
....................................."""
        output = """209"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
