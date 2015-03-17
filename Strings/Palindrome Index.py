def test(s):
    i=0
    j=len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return i
        i +=1
        j -=1
    else:
        return 0

t = int(input())
while t:
    t -= 1
    s=input()
    i=0
    j=len(s)-1
    while i <= j:
        if s[i] != s[j]:
            if s[i+1]==s[j]:
                result=test(s[:i]+s[i+1:])
                if result == 0:
                    print(i)
                    break
                else:
                    print(j)
                    break
            else:
                print(j)
                break
        i += 1
        j -= 1
    else:
        print("-1")