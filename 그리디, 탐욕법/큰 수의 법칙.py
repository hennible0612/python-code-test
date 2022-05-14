n, m, k, = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

print(first)
print(second)


result = 0

while m != 0:
    for i in range(k):
        result += first
        m -= 1
    result += second
    m -= 1

print(result)
