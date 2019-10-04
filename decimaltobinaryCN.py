x=int(input())
i=0#decimal to binary
sum=0
while (x>0):
	s=x%2
	sum=sum+((10**i)*s)
	x=x//2
	i=i+1

print(sum)