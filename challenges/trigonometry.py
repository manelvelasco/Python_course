# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:35:25 2013
@author: Manel
"""
def factorial(n):
    if n>1:
        res=n*factorial(n-1)
    else:
        res=1
    return res

def taylor_of_exponential(order=10):
    return lambda x: sum([x**k/factorial(k) for k in range(order+1)])

def sin(x,order=10):
    x=x%(2*3.14)
    csin=(taylor_of_exponential(order)(x*(1j))-taylor_of_exponential(order)(-x*(1j)))/(2j)
    return csin if isinstance(x, complex) else csin.real


def cos(x,order=10):
    x=x%(2*3.14)
    ccos=(taylor_of_exponential(order)(x*(1j))+taylor_of_exponential(order)(-x*(1j)))/(2.)
    return ccos if isinstance(x, complex) else ccos.real

def tan(x,order=10):
    try:
        return sin(x,order)/cos(x,order)
    except:
        return None

if __name__=="__main__":
    print sin(0)
    print tan(3,100)
    print cos(1)
    print sin(3)/cos(3)