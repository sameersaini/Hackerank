def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a = 0
    b = 1
    for _ in range(n):
        total = a + b
        b = a
        a = total
    return total

n = int(input())
print(fibonacci(n))
