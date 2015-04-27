for _ in range(int(input())):
	Str=input()

	KeyWord=''

	for x in Str:
		if x not in KeyWord:
			KeyWord += x

	alpha=''
	actual=''
	for x in range(ord('A'),ord('Z')+1):
		actual += chr(x)
		if chr(x) not in KeyWord:
			alpha += chr(x)


	New=''

	Temp=list(KeyWord)
	Temp.sort()

	for x in Temp:
		New +=x
		Index=KeyWord.find(x)
		for c in alpha[Index::len(KeyWord)]:
			New += c
	

	MAP={}

	for x in range(26):
		MAP[New[x]]=actual[x]

	

	for x in input():
		if x != ' ':
			print(MAP[x],end='')
		else:
			print(' ',end='')

	print()
	






