# 리스트
a = [1, 2, 3, 4]

# 리스트 선언
a = list()
a = []

# 리스트 초기화
b = [0] * 10
print(b)

# 리스트 뒤부터 출력
a = [1, 2, 3, 4]
print(a[-2])

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[0:4])

# 리스트 컴프리헨션
#        넣을값                   조건
array = [i for i in range(20) if i % 2 == 1]
arr = []
for i in range(20):
    if i % 2 == 1:
        arr.append(i)

print(array)
print(arr)

# 리스트 컴프리헨션 2차원 배열 초기화
n = 4
arr2 = [[0] * n for _ in range(4)]  # for i 써도 되는데 단숙 반복이므로 _ 사용
print(arr2)

# 리스트 관련 매서드
a = [1, 4, 3]

a.append(2)  # push O(1)
a.sort() # O(NlogN)
a.sort(reverse=True) # O(NlogN)
a.reverse() # O(N)
a.insert(2, 3)  # O(N)
p = a.count(3)  # 3 있는만큼 count  # O(N)
print(p)

a.remove(3)  # 맨앞에 있는거  # O(N)
print(a)

# 파이썬 removeall 이없음
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)
