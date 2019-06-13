n=int(input())
m=int(input())
k=input()
x=k.strip().split(" ")
x=[int(i) for i in x]
x=x[0:n*m]
y=[[x[i*m+j] for j in range(n)] for i in range(n) ]
for j in range(m):
	if j%2==0:
		for i in range(n):
			print(y[i][j],end=" ")
	else:
		for i in range(n-1,-1,-1):
			print(y[i][j],end=" ")