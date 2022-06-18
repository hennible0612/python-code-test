# 다익스타라 최단 경로 알고리즘
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3과 4번을 반복한다.

# 다익스타라 알고리즘은 최단 경로를 구하는 과정에서 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하면 리스트를 갱신한다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개술르 입력받기
n, m = map(int, input().split())
# 시작 노드 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한적이 있는지 체크하는 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijksta(start):
    q = []
    # 시작 노드에 대해서 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동한느 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijksta(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
