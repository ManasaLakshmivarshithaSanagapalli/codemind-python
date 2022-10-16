s=input().lower().split()
c=0;
for i in s:
    k=i;
    if k==k[::-1]:
        c=c+1
print(c)