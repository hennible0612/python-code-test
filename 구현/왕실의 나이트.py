x, y = list(input())
x = int(ord(x)) - int(ord('a'))
movement = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
counter = 0

for n, m in movement:
    if (int(x) + int(n) <= 8 and int(x) + int(n) >= 1 and int(y) + int(m) <= 8 and int(y) + int(m) >= 1):
        counter += 1

print(counter)
