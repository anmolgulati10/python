def spiralPrint(arr):
    # Please add your code here
    n=len(arr)
    m=len(arr[0])
    cs=0
    ce=m-1
    rs=0
    re=n-1
    count=0
    while (count<n*m):
	    for i in range(cs,ce+1):
	    	print(arr[rs][i],end=" ")
	    	count=count+1
	    rs=rs+1
	    for i in range(rs,re+1):
	    	print(arr[i][ce],end=" ")
	    	count=count+1
	    ce=ce-1
	    for i in range(ce,cs-1,-1):
	    	print(arr[re][i],end=" ")
	    	count=count+1
	    re=re-1
	    for i in range(re,rs-1,-1):
	    	print(arr[i][cs],end=" ")
	    	count=count+1
	    cs=cs+1
	    
    

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)
