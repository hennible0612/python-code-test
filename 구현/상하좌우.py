import math

n = int(input())
x = 1
y = 1
data = list(map(str, input().split()))

for i in data:

    if (i == 'R' and y + 1 <= n):
        y += 1
    elif (i == 'L' and y - 1 > 1):
        y -= 1
    elif (i == 'D' and x + 1 <= n):
        x += 1
    elif (i == 'U' and x - 1 > 1):
        x -= 1

print(x, y)

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
print(x, y)