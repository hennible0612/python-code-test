def solution(d, budget):
    d.sort()
    answer = 0
    counter = 0
    for i in d:
        counter += i
        answer += 1
        if budget < counter:
            answer -= 1
            break

    return answer


solution([2, 2, 3, 3], 10)
