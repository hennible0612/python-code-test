# itertools
# 파이썬에서 반복된느 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

# permutations 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일려로 나열하는 모든 경우(순열)을 계산해준다.
# permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

from itertools import permutations
data = ["A","B","C"]
result = list(permutations(data,2)) # 2 개를 뽑아 나오는 모든 경우 출력
print(result)

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는모든 경우를 계산한다.

from itertools import combinations
result = list(combinations(data,2))
print(result)

# product는 permutaions와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일려로 나열하는 모든 경우를 게산한다.
# 단, 원소를 중복하여 뽑는다.
from itertools import product
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의
# 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다.
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)