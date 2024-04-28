a=[4,3,2,1]
d=len(a)-1
b=[]
for i in range(len(a)):
    c=min(a)
    c,a[-1]=a[-1],c
    b.append(c)
    a.remove(c)
print(b)