from collections import deque

# bfs
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)

print(queue)
queue.reverse()
print(queue)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            queue.append(i)
            visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph, 1, visited)
