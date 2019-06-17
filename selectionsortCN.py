n=int(input())
x=input()
x=x.strip().split(" ")
x=[int(i) for i in x]



for i in range(n):
	min=x[i]
	for k in range(i,n):
		if x[k]<=min:
			min=x[k]
	y=x.index(min)
	temp=x[i]
	x[i]=x[y]
	x[y]=temp


	
print(x)
