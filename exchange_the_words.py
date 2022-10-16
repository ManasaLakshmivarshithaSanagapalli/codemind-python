n=input().split()
l=[]
for i in range(len(n)-1,-1,-1):
    k=n[i]
    l.append(k)
for i in l:
    print(i,end=" ")