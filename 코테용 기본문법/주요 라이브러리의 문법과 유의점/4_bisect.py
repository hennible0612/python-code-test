# 파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.
# bisect 라이브러리는 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
# bisect 라이브러리에서는 bisect_left() 함수와 bisect_right() 함수가 가장 중요하게 사용된다.


from bisect import bisect_left, bisect_right

# bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
# bisect_right(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(right_index)
    print(left_index)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 사이
