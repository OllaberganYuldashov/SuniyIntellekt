import math
import numpy as np


def Sigmoid(x):
    return 1 / (1 + np.exp(-x))

"""
# Sath aktivlashtirish funksiyasi
def BinaryStepFunc(x):
    if x>0:
        return 1
    else:
        return 0
"""

# Xatoliq funksiyasi
def mse(target, output):
    return 0.5 * math.pow(target-output,2)

# input - kiruvchi qiymatlar
x=np.array([[0],[1]])
#print('x=',x)

target=1

# weight - vazn koeffitsentlari
w=np.array([np.random.random(),np.random.random()])
print('o`qitishdan oldingi vazn koeffitsentlar:')
print(w)

l_rate=0.1

#print(np.dot(w,x))
output=Sigmoid(np.dot(w,x))
#print(output)

eror=mse(target,output)
#print(eror)

while eror>0.0000000001:
    abs_error=output-target
    d_w=abs_error*x
    w=w-l_rate*np.array(d_w).transpose()

    output=Sigmoid(np.dot(w,x))
    eror=mse(target,output)

print('o`qitish tugadi')
print(w)
print(output)




