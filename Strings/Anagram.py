t=int(input())
while t > 0:
    t -= 1
    fullstr=input()
    if len(fullstr) % 2 == 1 :
        print(-1)
        continue
    strA=fullstr[:len(fullstr)//2]
    strB=fullstr[len(fullstr)//2:]
    countA=[int(0) for i in range(26)]
    countB=[int(0) for i in range(26)]
    for i in strA:
        countA[ord(i)-97] += 1
    for i in strB:
        countB[ord(i)-97] += 1 
    count=0
    for i in range(26):
        diff=abs(countA[i]-countB[i])
        count += diff
    print(count//2)    