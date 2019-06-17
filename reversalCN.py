x=input()
x=x.split(" ")
y=[]
print(x)
for i in x:
    i=list(i)
    i.reverse()
    i="".join(i)
    i=str(i)
    y.append(i)
y=" ".join(y)
print(y)    


    

