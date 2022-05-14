n, m = map(int, input().split())

counter = 0

while n != 1:
    if n % m == 0:
        n = n // m
        counter += 1
    else:
        counter += 1
        n = n - 1

print(counter)