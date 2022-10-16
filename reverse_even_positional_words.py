n=input().split()
l=[]
for i in range(len(n)):
    if(i%2!=0):
        l.append(n[i])
    else:
        k=n[i];
        k=k[::-1]
        l.append(k)
for i in l:
    print(i,end=" ")