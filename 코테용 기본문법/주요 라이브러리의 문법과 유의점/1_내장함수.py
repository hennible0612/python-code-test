# 내장 함수

# sum
result = sum([1, 2, 3, 2, 4, 12])
print(result)

# min max
result = min([2, 4, 5, 6])
print(result)
result = max(2, 4, 5, 6)
print(result)

# eval
# 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
result = eval("(3+5)*7")
print(result)

# sorted
result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

# 튜플도 가능
result = sorted([("홍길동", 46), ("홍무무", 30), ("김디디", 50)], key=lambda x: x[1])
print(result)

