# import sys
# array = list(map(int, sys.stdin.readline().split()))
# print(array)


n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()
print(arr)
for i in range(n):
    print(i)

    print(arr[i][0], arr[i][1])
