import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    H, W = map(int, input().split())
    graph = []
    for i in range(H):
        s = input()
        if "s" in s:
            start_point = [i, s.index("s")]
        if "g" in s:
            goal_point = [i, s.index("g")]
        graph.append(s)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def DFS(graph, start_point, goal_point):
        not_visited = []
        not_visited = [[True for i in range(W)] for j in range(H)]
        stack = [start_point]
        not_visited[start_point[0]][start_point[1]] = False
        while len(stack) != 0:
            now_point = stack.pop()
            for i in range(4):
                if now_point == goal_point:
                    print("Yes")
                    return False
                else:
                    serch_point = [now_point[0] + dx[i], now_point[1] + dy[i]]
                    if 0 <= serch_point[0] < H and 0 <= serch_point[1] < W:
                        if graph[serch_point[0]][serch_point[1]] != "#" and not_visited[serch_point[0]][serch_point[1]]:
                            stack.append([serch_point[0], serch_point[1]])
                            not_visited[serch_point[0]][serch_point[1]] = False
        return True

    if DFS(graph, start_point, goal_point):
        print("No")


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
