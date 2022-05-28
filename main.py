# import sys
# array = list(map(int, sys.stdin.readline().split()))
# print(array)
#
# array2 = set(map(int, input().split()))
# print(array2)
import sys

sys.setrecursionlimit(10000)
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]


def dfs(i, j):
    for l in range(8):
        x = i + dx[l]
        y = j + dy[l]
        if 0 <= x < m and 0 <= y < n and graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x, y)


answer_arr = []
while True:
    n, m = map(int, input().split())
    graph = []
    if n == 0 and m == 0:
        break

    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))
    answer = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                answer += 1
                graph[i][j] = 0
                dfs(i, j)

    print(answer)
