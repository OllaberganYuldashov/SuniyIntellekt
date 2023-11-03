a=12
if a>0:
    print('musbat')
    print(a)
else:
    print('manfiy')
    print(a)


print('musbat') if a>0  else print('manfiy')



if a>0:
    print('musbat')
else:
    if a<0:
        print("manfiy")
    else:
        print('null')

print('musbat') if a>0 else print('manfiy')  if a<0 else print('null')

a=12
b=23

if  a>0 and b>0:
    print('2 alasi ham musbat')
elif a>0 or b>0:
    print('1 tasi musbat')
else:
    print('2 alasi ham manfiy')

l=[1,2,5,0,4,7]
if 2 in l:
    print('mavjud')

l1=[1,2,3]
l2=[[0,4],[1,2,3],[4,5,6]]
if l1 in l2:
    print('Yes')
