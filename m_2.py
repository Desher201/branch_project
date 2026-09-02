l = [1,2,3,4]
l+=[5,6,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
for i in [5,6,7,8]:
    if i in l :
        while i in l:
            l.remove(i)
print(l)