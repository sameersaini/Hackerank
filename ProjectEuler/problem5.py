def gcd(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


lcm = (1*2)//gcd(1,2)

for i in range(3, 20):
    lcm = (i * lcm) // gcd(i, lcm)

print(lcm)
