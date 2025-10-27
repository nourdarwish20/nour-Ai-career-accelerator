def newlist(a):
    t=[]
    t.append(a[0])
    t.append(a[-1])
    return t
    
a = [5, 10, 15, 20, 25]
res=newlist(a)
print(res)