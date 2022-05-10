a = 0


def func():
    global a  # 전역 참조
    a += 1


for i in range(10):
    func()

print(a)

# 람다식
#           매개변수 : return 값
add = lambda a, b: a + b
print((lambda a, b: a + b)(3, 7))
print(add(3, 3))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(add,list1,list2) # map 리스트의 요소를 지정된 함수로 처리해주는 함수
print(list(result))
