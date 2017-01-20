from numpy import *

a = array([[3., 1., 2.], 
			[1., 2., -1.], 
			[3., 2., -5.]])

b = [21., 13., -1.]

n = linalg.matrix_rank(a)

def norma_matr(matr):
	return max(abs(matr.max()), abs(matr.min()))
	
def eps(matr, normaxi):
	return norma_matr(matr) / (1 - norma_matr(matr)) * max(normaxi)

def m_prost_iter(a, b, n):
	c, d = peretv_matr(a, b, n)
	xk = [0] * n
	xk1 = [0] * n
	normax = [0] * n
	count = 0
	e = 1
	while e >= 1.e-6:
		for i in range(0,n):
			xk1[i] = d[i]
			for j in range(0,n):
				xk1[i] += c[i,j] * xk[j]
			normax[i] = abs(xk1[i] - xk[i])
		e = eps(c, normax)
		count += 1
		xk = copy(xk1)
	print("eps =", e, 'k-st iter =', count, "\nxk1:", xk1)
	return xk1


def m_Zeyd(a, b, n):
	c, d = peretv_matr(a, b, n)
	xk = [0] * n
	xk1 = [0] * n
	normax = [0] * n
	count = 0
	e = 1
	while e >= 1.e-6:
		for i in range(0, n):
			xk1[i] = d[i]
			for j in range(0, i):
				xk1[i] += c[i,j] * xk1[j]
			for j in range(i+1, n):
				xk1[i] += c[i,j] * xk[j]
			normax[i] = abs(xk1[i] - xk[i])
		e = eps(c, normax)
		count += 1
		xk = copy(xk1)
	print("eps =", e, "k-st iter m. Zeyd. =", count, "\nxk1: ", xk1)
	return xk1
		
def peretv_matr(a, b, n):
	c = empty([n, n])
	d = copy(b)
	for i in range(0, n):
		d[i] = b[i] / a[i,i]
		for j in range(0, n):
			c[i,j] = -a[i,j] / a[i,i]
		c[i,i] = 0
	return c, d
	
print("m_PROSTOYI_ITERATSII: ")
m_prost_iter(a, b, n)
print()
print("m_ZEYDELYA: ")
m_Zeyd(a, b, n)
	

def perevirka(matr, list_b, xarr, n):
	for i in range(0,n):
		sum = 0
		for j in range(0,n):
			sum += matr[i,j] * xarr[j] 
		print(sum, '=', b[i])
	
print ("\nPerevirka koreniv m-du prost. iter.:")
perevirka(a, b, m_prost_iter(a, b, n), n)
print ("\nPerevirka koreniv m-du Zeyd.:")
perevirka(a, b, m_Zeyd(a, b, n), n)