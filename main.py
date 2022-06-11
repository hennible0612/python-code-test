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

n = int(input())

zero_dp = [1, 0, 1]

one_dp = [0, 1, 1]


def fibo(x):
    if len(zero_dp) <= x:
        for i in range(len(zero_dp), x + 1):
            zero_dp.append(zero_dp[i - 1] + zero_dp[i - 2])
            one_dp.append(one_dp[i - 1] + one_dp[i - 2])


for _ in range(n):
    num = int(input())
    fibo(num)
    print(zero_dp[num], one_dp[num])

# print(fibo(22))
