x=[9,8,7,6,5,4,3,2,1]
for j in range(len(x)):
	for i in range(len(x)-1):
		if x[i+1]<=x[i]:
			temp=x[i+1]
			x[i+1]=x[i]
			x[i]=temp
print(x)
