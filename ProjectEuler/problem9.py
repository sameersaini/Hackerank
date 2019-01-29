"""
For any two numbers m and n with n>m, pythagorean triplet can be found using
a = (n ** 2 + m ** 2)
b = 2 * n * m
c = (n ** 2 - m ** 2)
"""

n = 2
while True:
    found = False
    for m in range(n):
        a = (n ** 2 + m ** 2)
        b = 2 * n * m
        c = (n ** 2 - m ** 2)

        if a+b+c > 1000:
            break

        if a+b+c == 1000:
            found = True
            print([a,b,c])
            print(a*b*c)
            break

    if found:
        break

    n+=1
