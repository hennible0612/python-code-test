
# https://www.acmicpc.net/problem/2667
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

m = len(graph[0])

answer = 0
counter = 0

list_answer = []



def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        global counter
        counter += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1
            list_answer.append(counter)
            counter = 0

list_answer.sort()
print(answer)
for i in range(len(list_answer)):
    print(list_answer[i])


# print(graph)





from collections import deque

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    counter = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                counter += 1
    return counter

answer_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer_list.append(bfs(i,j))

answer_list.sort()
print(len(answer_list))
for i in range(len(answer_list)):
    print(answer_list[i])