score = 85

result = "success" if score >= 80 else "fail"
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)
