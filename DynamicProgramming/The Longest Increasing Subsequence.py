def ceilIndex(L,l,r,key):
	while r-l > 1:
		m = l + (r-l)//2
		if L[m] >= key:
			r = m
		else:
			l=m
	return r


def LIS(A):
	tailTable=[]
	tailTable.append(A[0])
	Len=1
	for i in range(1,len(A)):
		if A[i] < tailTable[0]:
			tailTable[0]=A[i]
		elif A[i] > tailTable[-1]:
			Len += 1
			tailTable.append(A[i])
		else:
			tailTable[ceilIndex(tailTable,-1,Len-1,A[i])]=A[i]
	return Len

print(LIS([int(input()) for i in range(int(input()))]))
