n=int(input())

def get_primes(n):
    primes=[1 for i in range(n+1)]
    for i in range(2,n):
        if  i*i > n:
            break
        else:
            for j in range(i,n):
                if i*j > n:
                    break
                else:
                    primes[i*j]=0
    return primes
def get_multiplicity(primes,n):
    total=1
    multiplicity=[1 for i in range(n+1)]
    for i in range(2,len(primes)):
        if primes[i]==1:
            temp=n
            power=0
            while temp>1:
                power += temp//i
                temp = temp//i
            total *= (2*power+1)
    return total
primes=get_primes(n)
multiply=get_multiplicity(primes,n)
print(multiply%1000007 )
