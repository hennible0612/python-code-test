
# input
data = list(map(int, input().split()))
print(data)

n, m, k = map(int, input().split())
print(n, m, k)

# input속도가 느림 만약 많은 입력을 받아야한다면
# 아래 코드 사요ㅕㅇ
import sys
sys.stdin.readline().rstrip() # rstrip는 줄바꿈 기호 자르는 용도

#f string
answer = 7
print(f"정답은 {answer} 이비니다.")
