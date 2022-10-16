n=input().lower().split()
p=input().lower().split()
c=0;
for i in n:
    for j in p:
        if(i==j):
            c=c+1;
print(c)