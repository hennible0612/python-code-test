import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

test_case = int(input())

for _ in range(test_case):
    answer = 0

    n, m, l = map(int,input().split())
    graph = [[0]*n for _ in range(m)]


    for _ in range(l):
        a, b = map(int, input().split())
        graph[b][a] = 1


    for i in range(n):
        for j in range(m):
            if True == dfs(i,j):
                answer += 1


    print(answer)