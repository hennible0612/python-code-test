def dfs(network, v, visited):
    if visited[v]:
        return False

    visited[v] = True

    for i in network[v]:
        dfs(network, i, visited)

    return True


def solution(n, computers):
    answer = 0
    network = [[] for _ in range(n + 1)]
    visited = [False] * int(n + 1)

    for i, node in enumerate(computers):
        for j, item in enumerate(node):
            if item == 1 and i != j:
                network[i + 1].append(j+1)

    for i in range(1, n + 1):
        if dfs(network, i, visited):
            answer += 1

    return answer


solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
