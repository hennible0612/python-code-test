# n, m = map(int, input().split())
num = int(input())
answer = 0
i = 1
while True:

    num -= i
    if num >= 0:
        answer += 1
        i += 1
    else:
        print(answer)
        break
