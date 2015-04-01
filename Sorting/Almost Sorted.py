n=input()
numbers=[int(x) for x in input().split()]
new = sorted(numbers)
if new == numbers : print("yes")
else:
    flag=0
    i=0
    j=len(numbers)-1
    while numbers[i+1] > numbers[i]:i += 1
    while numbers[j-1] < numbers[j]:j -= 1
    temp=numbers[:]
    temp[i]=temp[i]^temp[j]
    temp[j]=temp[i]^temp[j]
    temp[i]=temp[i]^temp[j]
    if temp == new:
        print("yes")
        print("swap {} {}".format(i+1,j+1))
        flag=1
    else:
        temp=numbers[:i] + list(reversed(numbers[i:j+1])) + numbers[j+1:]
        if temp == new:
            print("yes")
            print("reverse {} {}".format(i+1,j+1))
            flag=1
if flag==0:
    print("no")