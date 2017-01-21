from num_meths import *
import time

a = float(input("a=")) # 1
b = float(input("b=")) # 2
e = 1e-06

if f(a) * f(b) >= 0: print( "Неправильно вибраний вiдрiзок iзоляцii")

print("e =", e)
print("f({0})={1}".format(a, f(a)))
print("f({0})={1}".format(b, f(b)))

print()
print ("---METOD POLOVYNNOGO PODILU---")    
t1 = time.clock()
m_pol_pod(a, b, e)
t2 = time.clock()
print ("t =", t2 - t1)


print()
print ("---METOD NEWTONA (DOTYCHNYH)---")    
t1 = time.clock()
m_newtona(a, b, e)
t2 = time.clock()
print ("t =", t2 - t1)


print()
print ("---METOD HORD---")    
t1 = time.clock()
m_hord(a, b, e)
t2 = time.clock()
print ("t =", t2 - t1)


print()
print ("---METOD SICHNYH---")    
t1 = time.clock()
m_sichnyh(0.5, 1.1, e)
t2 = time.clock()
print ("t =", t2 - t1)


print()
print ("---METOD PROSTOYI ITERATCII---")    
t1 = time.clock()
m_iter(a, b, e)
t2 = time.clock()
print ("t =", t2 - t1)


print()
print ("---METOD DOTYCHNYH I HORD---")    
t1 = time.clock()
m_dot_i_hord(a, b, e)
t2 = time.clock()
print ("t =", t2 - t1)