#아이디의 길이는 3~15
#알파벳 소문자, 숫자, -, _, .    but . 은 마지막에 사용불가능 연속 사용불가능

def solution(new_id):
    answer = ""
    temp = ""
    # 1단계 소문자
    temp = new_id.lower()
    # 2단계 특수문자 제거
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i


    print(answer)



    return answer


lottos = [1, 2, 6, 9, 10, 18]
win_nums = [20, 9, 3, 45, 4, 35]

solution("...!@BaT#*..y.abcdefghijklm")
# solution("ABCDEFG")
