import math

arr = list(map(int, input().split()))
answer = 0

for i in arr:
    answer += i * i
print(answer % 10)
