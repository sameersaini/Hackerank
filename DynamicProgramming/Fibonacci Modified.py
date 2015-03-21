
line=input()
(a,b,n)=line.split()
a=int(a)
b=int(b)
n=int(n)


i=3

while(i<=n):
	new=b*b+a
	a=b
	b=new
	i=i+1
	
print (new)
