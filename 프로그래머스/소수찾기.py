from itertools import permutations

def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        result.append(list(set(map(''.join, permutations(numbers, i)))))
    result = sum(result, [])

    result = list(set(map(int, result)))

    answer = 0
    for i in result:
        if is_prime_number(int(i)):
            answer += 1
    return answer




solution("011")
# 1 4 10 12