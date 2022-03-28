# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections

def solution(id_list, report, k):
    report = set(report)  # 신고 리스트 중복제거
    reported_dict = dict.fromkeys(id_list, 0)
    answer = [0] * len(id_list)  # id 길이만큼 배열초기화

    for user in report:  # 신고 목록 정리
        reporter, reported = user.split()
        reported_dict[reported] = reported_dict[reported] + 1

    for user in report:
        reporter, reported = user.split()
        if (reported_dict[reported] >= k):  # 신고 목록에서 k 보다 크거나 같으면
            index = id_list.index(reporter)  # 신고한 유저의 배열 위치
            answer[index] = answer[index] + 1
    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "muzi neo", "apeach frodo", "apeach muzi", "frodo neo"]
k = 2

solution(id_list, report, k)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
