# import sys
# from collections import deque
#
# n = int(input())
#
# for _ in range(n):
#     length, target = map(int, sys.stdin.readline().split())
#     data = deque(map(int, sys.stdin.readline().split()))
#
#     maxNum = 0
#     counter = 0
#     while True:
#         maxNum = max(data)
#         firstNum = data.popleft()
#         if firstNum == maxNum:
#             counter += 1
#             if target == 0:
#                 break
#         else:
#             data.append(firstNum)
#         target = target - 1;
#         if target == -1:
#             target = length - 1
#
#     print(counter)
#

# n = int(input())
# answer_list = []
# for _ in range(n):
#     h, w, t = map(int, input().split())
#     floor = t % h
#
#     num = t // h + 1
#
#     if t % h == 0:
#         floor = h
#         num = t // h
#
#     answer_list.append(100 * floor + num)
#
# for answer in answer_list:
#     print(answer)

# n = int(input())
#
# zero_dp = [1, 0, 1]
#
# one_dp = [0, 1, 1]
#
#
# def fibo(x):
#     if len(zero_dp) <= x:
#         for i in range(len(zero_dp), x + 1):
#             zero_dp.append(zero_dp[i - 1] + zero_dp[i - 2])
#             one_dp.append(one_dp[i - 1] + one_dp[i - 2])
#
#
# for _ in range(n):
#     num = int(input())
#     fibo(num)
#     print(zero_dp[num], one_dp[num])

# print(fibo(22))


#
# n = int(input())
#
# list = [0] * 301
# dp = [0] * 301
#
# for i in range(n):
#     list[i] = int(input())
#
# dp[1] = list[1]
# dp[2] = list[1] + list[2]
#
# for i in range(3, n):
#     dp[i] = max(list[i] + list[i - 1] + dp[i - 3], list[i] + dp[i - 2])
#
# print(dp[n])
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
