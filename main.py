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

def fibo(x):

    if x == 1 or x == 2:
        return 1
    tmp = fibo(x-1) + fibo(x-2)
    return tmp

print(fibo(100))

