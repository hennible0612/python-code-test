
# https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, k):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] > k and visited[x][y] == 1:
        visited[x][y] = 0
        dfs(x - 1, y, k)
        dfs(x + 1, y, k)
        dfs(x, y - 1, k)
        dfs(x, y + 1, k)

        return True
    return False


n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

m = len(graph[0])

answer = 0
answer_arr = []


for k in range(max(map(max, graph))):
    answer = 0
    visited = [[1] * n for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if dfs(i, j, k):
                answer += 1

    answer_arr.append(answer)

print(max(answer_arr))
