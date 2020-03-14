import collections
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    H, W = map(int, input().split())
    l = [input() for _ in range(H)]
    s_h = 0
    s_w = 0

    # sの位置を調べる
    for i in range(H):
        if "s" in l[i]:
            s_h = i
            s_w = l[i].index("s")

    # sの位置だけ入っているようにする
    stack = collections.deque([[s_h, s_w]])

    # すべてが0(いったことがないマス)にする
    visited = [[0] * W for _ in range(H)]
    # スタートの位置はいったことがあるマスに
    visited[s_h][s_w] = 1
    check = False
    # キューに入っていればずっと続ける
    while len(stack) > 0:
        h, w = stack.pop()
        if l[h][w] == "g":
            check = True
        # 上下左右4方向を調べる
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_h, new_w = h + j, w + k
            # 枠外だったら次に
            if new_h < 0 or new_h >= H or new_w < 0 or new_w >= W:
                continue
            # 壁じゃないかつ、いったことがなければキューに追加
            if l[new_h][new_w] != "#" and visited[new_h][new_w] == 0:
                visited[new_h][new_w] = 1
                stack.append([new_h, new_w])
    print("Yes" if check else "No")


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
        input = """4 5
s####
....#
#####
#...g"""
        output = """No"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """4 4
...s
....
....
.g.."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#..."""
        output = """No"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input5(self):
        print("test_input5")
        input = """1 10
s..####..g"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
