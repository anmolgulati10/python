x=int(input())
x=0
for i in range(2,x+1):
	for j in range(2,i):
		if i%j==0 and i!=j:
			break
		
		else:
			print(i)
			
