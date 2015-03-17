L=''.join(input().split())
Temp=[0 for _ in range(26)]
for char in L:
    if ord(char) > 90:
        Temp[97-ord(char)]=1
    else:
        Temp[65-ord(char)]=1
for x in Temp:
    if x==0:
        print("not pangram")
        break
else:
    print("pangram")