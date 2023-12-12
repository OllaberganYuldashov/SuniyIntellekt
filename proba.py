
try:
    l=[1,2,3,4]
    print(l[1])
    print(12/0)
    f=open('asd.txt')
except IndexError:
    print('indeksdan chiqib ketdi')
except ZeroDivisionError:
    print('nolga bo`lib bo`lmaydi')
except Exception as ex :
    print(ex)