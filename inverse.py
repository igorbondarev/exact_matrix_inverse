from sympy import Matrix, pprint

dimension = 2

mat = [[0 for x in range(dimension)] for y in range(dimension)]
b   = [0 for x in range(dimension)]
p   = 5
m   = 10

mat[0][0] = -10
mat[0][1] = 12
mat[1][0] = 16
mat[1][1] = -27

b[0] = -4
b[1] = 8

def print_matrix(m, n):
	for i in range(n):
		for j in range(n):
			print m[i][j],
		print ""

def print_vector(v, n):
	for i in range(n):
		print v[i],
	print ""

def mod(val, m):
	if val == 0:
		return 0
	if val < 0:
		val = -val
		if ((val % m) == 0):
			return 0
		return m - val % m
	if val > 0:
		return val % m

def matrix_by_mod(m, modulo, n):
	for i in range(n):
		for j in range(n):
			m[i][j] = mod(m[i][j], modulo)
		
#print "Matrix A:"
#print_matrix(mat, dimension)
#print "Vector b:"
#print_vector(b, dimension)
#print "Ap:"
#matrix_by_mod(mat, p, dimension)
#print_matrix(mat, dimension)

A = Matrix([
    [0,2],
    [1,3]
])

#Find inverse of A modulo 26
A_inv = A.inv_mod(5)
pprint(A_inv)

