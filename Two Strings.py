t=int(input())
for _ in range(t):
    A=input()
    B=input()
    La=[int(0) for x in range(26)]
    Lb=[int(0) for x in range(26)]
    
    for x in A:
        La[ord(x)-97]=1
    for x in B:
        Lb[ord(x)-97]=1
    
    for i in range(26):
        if La[i]==1 and Lb[i]==1:
            print("YES")
            break
    else:
        print("NO")