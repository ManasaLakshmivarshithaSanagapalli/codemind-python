n=input()
b=[]
for i in n:
    if i not in b:
        b.append(i)
if(len(b)==len(n)):
    print("True")
else:
    print("False")