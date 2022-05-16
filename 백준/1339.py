dict = dict()


n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for word in arr:
    for i in range(len(word)):

        if word[i] in dict:
            dict[word[i]] += 10 ** (len(word)-i-1)
        else:
            dict[word[i]] = 10 ** (len(word)-i-1)

list = []
for num in dict.values():
    list.append(num)
list.sort(reverse=True)

answer = 0
counter = 9
for i in list:
    answer += counter * i
    counter = counter - 1
print(answer)
