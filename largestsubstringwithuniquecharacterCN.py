x=input()
y=list(x)
z=[]
a=[]
for i in range(len(y)):
	z=[]
	for j in range(i,len(y)):
		if y[j] not in z:
			z.append(y[j])
		else:
			break
	if len(z)>len(a):
		a=z

a="".join(a)
print(a)