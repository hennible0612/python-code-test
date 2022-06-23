# 모든 노드에서 다른 노드까지의 최단 경로를 모두 계산합니다.
# 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마친가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행합니다.
#   다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않습니다.
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기'
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받ㅇ, 그 갋ㅅ으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
