list2 = [1, 2, 3, 4, 5]
k = 2

output = []
temp = []

def follow_1():
    global output, temp
    for x, num in enumerate(list2):
        if num % k == 0:
            temp = output[:x]
            temp = list(reversed(temp))
            output[:x] = temp
        output.append(num)
    return output

print(follow_1())