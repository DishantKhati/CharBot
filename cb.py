s,a,k,l,t=input("Enter the string: "),[],65,48,[]
c0,d0=0,0
for i in range(6):
    c=[]
    for j in range(6):
        if k<=90:
            c.append(chr(k))
            k+=1
        else:
            c.append(chr(l))
            l+=1
    a.append(c)
for n in s:    
    for i in range(6):
        for j in range(6):
            if n==a[i][j]:
                c,d=i,j
                c1,d1=c-c0,d-d0
                if d<d0:
                    for u in range(d1*-1):
                        t.append('L')
                if c>c0:
                    for u in range(c1):
                        t.append('D')
                if d>d0:
                    for u in range(d1):
                        t.append('R')
                if c<c0:
                	for u in range(c1*-1):
		                t.append('U')
                t.append('S')
                c0,d0=c,d
print("Bot Command: ",end='')
for i in range(len(t)):
    if i==(len(t)-1):
        print(t[i])
    else:    
        print(t[i],end=' , ')
	
