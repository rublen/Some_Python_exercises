from math import sqrt

def f(x):
    return x**2 * sqrt((x**4)+1) - 1.5
    #return 2*x + 3

def poh1_f(x):
    return (4*x**5+2*x)/sqrt((x**4)+1)
    
def poh2_f(x):
    return (12 * x**8 + 9 * x**4 + 1) / pow((x**4)+1, 3/2)

def printing(x, poh, counter):    
    print('x =', x)
    print ("pohybka =", poh)
    print("f(x)=", f(x))
    print ("Kilkist iteratciy:", counter)

    
def m_pol_pod(a, b, e):    
    counter = 0
    x = (a + b) / 2.0
    poh = abs(b - a) / 2.0
    while poh > e:
        if f(a) * f(x) <= 0: b = x 
        elif f(x) * f(b) <= 0: a = x
        x = (a + b) / 2.0
        poh = abs(b - a) / 2.0
        counter  += 1    
    printing(x, poh, counter)

def xk_md(x1):
    return x1 - f(x1)/poh1_f(x1)

def m_newtona(a, b, e):
    counter = 0
    x1 = (a + b) / 2.0
    x2 = xk_md(x1)
    while abs(x2 - x1) > e:
        x1 = x2
        x2 = xk_md(x1)
        counter += 1
    printing(x2, abs(x2 - x1), counter)
     
    
def xk_mh(x, c):
    return x - f(x) / (f(x) - f(c)) * (x - c)
   
def m_hord(a, b, e):
    counter = 0
    x1 = (a + b) / 2.0
    if f(a) * poh2_f(a) > 0: c = a
    elif f(b) * poh2_f(b) > 0: c = b
    else: print ("Неправ.вiдр.iзоляц.")
    x2 = xk_mh(x1, c)
    while abs(x2 - x1) >= e:
        x1 = x2
        x2 = xk_mh(x1, c)
        counter += 1
    printing(x2, abs(x2 - x1), counter)
    

def xk_ms(x0, x1):
    return x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0)
   
def m_sichnyh(a, b, e):
    counter = 0
    x0 = a
    x1 = b
    x2 = xk_ms(x0, x1)
    while abs(x2 - x1) > e:
        x0 = x1
        x1 = x2
        x2 = xk_ms(x0, x1)
        counter += 1
    printing(x2, abs(x2 - x1), counter)


def xk_mpi(x, c):
    return x - c * f(x)

def m_iter(a, b, e):
    x0 = (a + b) / 2
    counter = 0
    c = 2 / (poh1_f(0.8) + poh1_f(1.2))
    q = 0.6
    x1 = x0
    x2 = xk_mpi(x1, c)
    while q / (1 - q) * abs(x2 - x1) > e:
        x1 = x2
        x2 = xk_mpi(x1, c)
        counter += 1
    printing(x2, q / (1 - q) * abs(x2 - x1), counter)
    

def m_dot_i_hord(a, b, e):
    counter = 0
    if f(a) * poh2_f(a) > 0:
        xd = a
        xh = b   # c = xd
    elif f(b) * poh2_f(b) > 0:
        xd = b
        xh = a   # c = xd
    while abs(xd - xh) > e:
        xd = xk_md(xd)
        xh = xk_mh(xh, xd)
        counter += 1
    x = (xd + xh) / 2    
    printing (x, abs(xd-xh), counter)
    