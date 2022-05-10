# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 주의점 소수끼리 더할때 완벽하게 더하지 않음
a = 0.3 + 0.6  # 0.899...
print(a)
# 그래서 round를 사용한다.
print(round(a, 4))  # 5번째 자리부터 반올림한다
b = 0.63812
print(round(b, 2))  # 3번째 자리부터 반올림한다

# 나누기, 나머지, 몫
a = 7
b = 3
print(a / b)
print(a % b)
print(a // b)

# 거듭제곱
print(a ** b)

