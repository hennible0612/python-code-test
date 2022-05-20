# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i + 1 ,"번 째 함수를 호출합니다.")
#     recursive_function(i + 1)
#     print(i, "번째 재귀 함수를 종료합니다.")
#
# recursive_function(1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        print(i)
        result *= i
    return result

print("반복적으로 구현: ", factorial_iterative(5))



def factorial_recursive(n):
    if n < 1:
        return 1
    return n * factorial_recursive(n-1)

print("재귀적으로 구현: ", factorial_recursive(5))
