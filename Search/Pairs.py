"""
Problem Statement

Given N integers, count the number of pairs of integers whose difference is K.

Input Format
The first line contains N and K.
The second line contains N numbers of the set. All the N numbers are unique.

Output Format
An integer that tells the number of pairs of integers whose difference is K.

Constraints:
N=105
0<K<109
Each integer will be greater than 0 and at least K smaller than 2^31-1. 

"""

#			SOLUTION		#


N,K=(int(x) for x in input().split())

Numbers=[int(x) for x in input().split()]

Numbers.sort()
count=0
Start=1                                     #sort the numbers and start comparing numbers from index 1 then after it
for i in range(len(Numbers)):               #compare numbers from the last successful match .Here Start is used to  
    for j in range(Start,len(Numbers)):         #take care of that condition
        if Numbers[j]-Numbers[i]==K:
            count += 1
            Start=j+1
            break
        if Numbers[j]-Numbers[i]>K:
            break
        
print(count)