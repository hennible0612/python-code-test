n = int(input())
answer = []
for _ in range(n):
    m = int(input())
    tmp = ""
    num = 0
    for _ in range(m):
        uni, alc = input().split()
        if int(alc) >= int(num):
            tmp = uni
            num = alc

    answer.append(tmp)

for word in answer:
    print(word)

