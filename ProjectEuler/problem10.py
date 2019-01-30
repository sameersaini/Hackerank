twoMillion = 2000000
arr = [True for _ in range(twoMillion)]

sqrt = int(twoMillion ** 0.5) + 1

for number in range(2, sqrt):
    if arr[number]:
        for i in range(2 * number, len(arr), number):
            if arr[i]:
                arr[i] = False

arr[1] = False
arr[0] = False

print(sum([i for i in range(len(arr)) if arr[i]]))