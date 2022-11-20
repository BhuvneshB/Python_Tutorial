a=[3,5,1,6,7,2,9,0,4]
b=[[0],[1]]
while b[-2]!=b[-1]:
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
        else:
            pass
    b.append(str(a))
    print(a)
