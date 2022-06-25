
answer = []
while True:

    parenthesis_list = []
    brackets_list = []
    parenthesis = 0
    brackets = 0
    words = input()
    if words[0] == ".":
        break
    for i in words:
        if i == "(":
            parenthesis += 1
        elif i == ")":
            parenthesis -= 1
        elif i == "[":
            brackets += 1
        elif i == "]":
            brackets -= 1
        elif i == ".":
            if parenthesis == 0 and brackets == 0:
                answer.append("yes")
            else:
                answer.append("no")


for word in answer:
    print(word)


