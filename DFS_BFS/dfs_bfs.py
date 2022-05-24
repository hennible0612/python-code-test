# node 개수 n
# m 간선의 개수
# v 시작점

# https://www.acmicpc.net/problem/1260
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * int(n + 1)

bfs_answer = []
dfs_answer = []


def dfs(graph, v, visited):
    visited[v] = True
    dfs_answer.append(v)
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        bfs_answer.append(v)

        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
print()
visited = [False] * int(n + 1)
bfs(graph, v, visited)
