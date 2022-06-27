def solution(n):
    answer = ''

    while (n >= 1):
        re = n % 3
        n = n // 3
        answer += str(re)

    return int(answer, 3)



solution(2414)
