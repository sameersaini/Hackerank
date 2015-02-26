t=int(input())
while t> 0:
    t -= 1
    number=int(input())
    i=0
    while i < 32:
        number = number ^ 1 << i
        i += 1
    print(number)    
    