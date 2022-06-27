n = input()
n = sorted(n, reverse=True)
answer = 0


for i in n:
    answer += int(i)

if answer % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))
