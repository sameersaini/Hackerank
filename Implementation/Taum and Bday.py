t=int(input())
for _ in range(t):
    B,W=(int(x) for x in input().split())
    X,Y,Z=(int(x) for x in input().split())
    amount=B*X + W*Y
    
    B_converted=B*Z +(B+W)*Y
    
    if amount > B_converted:
        amount=B_converted
    W_converted=W*Z + (B+W)*X
    if amount > W_converted:
        amount=W_converted
    print(amount)