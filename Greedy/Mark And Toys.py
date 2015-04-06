N,K=(int(x) for x in input().split())

Prices=[int(x) for x in input().split()]

Prices.sort()

current_sum=0
bought=0

for price in Prices:
    current_sum += price
    if current_sum <= K:
        bought += 1
    else:
        break
    
print(bought)
        