n=int(input())
c=0
p=0
dc=0
while(n!=0):
    d=n%10;
    n=n//10;
    dc=dc+1
    if(d%2==0):
        c=c+1;
    else:
        p=p+1;
if(dc==c):
    print("Even")
elif(dc==p):
    print("Odd")
else:
    print("Mixed")
        
    