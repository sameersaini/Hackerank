def fibo():
    a = 0
    b = 1

    sum = 0
    ans = 0
    while sum <= 4000000:
        if sum % 2 == 0:
            ans += sum

        sum = a + b
        a = b
        b = sum

    print(ans)

fibo()