def solution(lottos, win_nums):
    answer = [0] * 2
    zero_num = lottos.count(0)
    counter = 0  # 똑같은 숫자의 갯수
    for i in win_nums:
        if i in lottos:
            counter += 1

    if zero_num == 6:
        answer = [1,6]
    elif counter == 0 and zero_num ==0:
        answer = [6,6]
    elif counter == 6 :
        answer = [1,1]
    else:
        answer = [7-(zero_num+counter), 7-counter]

    return answer


lottos = [1, 2, 6, 9, 10, 18]
win_nums = [20, 9, 3, 45, 4, 35]

solution(lottos, win_nums)
