import sys

# n = int(input())


answer = []

# command = sys.stdin.readline().split()
command = input()
m = int(input())
num_list = input().rstrip()[1:-1].split(",")






for i in range(len(command)):
    if command[i] == "R":
        num_list.reverse()
    elif command[i] == "D":
        if len(num_list) > 1:
            del num_list[0]
        else:
            answer.append("error")
            break
    if len(num_list) > 0:
        answer.append(num_list)

print(answer)