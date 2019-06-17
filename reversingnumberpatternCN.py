n=int(input())
a=0
m=1
for i in range(1,n+1):
	if i%2!=0:
		for j in range(i):
			a=a+1
			print(a,end="")
		a=a+2*m
		m=m+1
	else:
		for k in range(i):
			print(a,end="")
			a=a-1
		a=a+i
	print()
	

	
