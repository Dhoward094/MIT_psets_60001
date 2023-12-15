list1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
output = []

def sorting():
    for num in list1:
        for x in num:
            output.append(x)
    output.sort()
    return output
print(sorting())