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

b[0] = 0
b[1] = 1

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

def matrix_by_mod(m, modulo):
	ret = [[0 for x in range(len(m))] for y in range(len(m))]
	for i in range(len(m)):
		for j in range(len(m)):
			ret[i][j] = mod(m[i][j], modulo)
	return ret

def vec_by_mod(vec, modulo):
	ret = [0 for x in range(len(vec))]
	for i in range(len(vec)):
		ret[i] = mod(vec[i], modulo)
	return Matrix(ret)
		
print "Matrix A:"
print mat
print "Vector b:"
print b
print "Ap:"
mod_matrix = matrix_by_mod(mat, p)
print mat

A = Matrix(mod_matrix)
A_inv = A.inv_mod(5)
new_mat = [[A_inv[y, x] for x in range(len(mat))] for y in range(len(mat))]
print "Cp:"
print new_mat

print "Starting math"
print "*************"
print ""

bk =  [0 for x in range(m + 1)]
bkp = [0 for x in range(m + 1)]
xkp = [0 for x in range(m + 1)]
Matrix_Cp = Matrix(new_mat)
Matrix_A = Matrix(mat)
bk[0] = Matrix(b)
Z = Matrix([[0], [0]])


for k in range(m):
	bkp[k] = vec_by_mod(bk[k], p)
	xkp[k] = vec_by_mod(Matrix_Cp * bkp[k], p)
	bk[k + 1] = (bk[k] - Matrix_A * xkp[k]) / p

	print k
	print bkp[k]
	print xkp[k]
	print bk[k + 1]

print "Calc Z"
print "******"

for k in range(m):
	Z = Z + (p ** k) * xkp[k]

print Z

def restore(vecz):
	for val in vecz:
		u = []
		v = []

		u.append(p ** m)
		u.append(val)

		v.append(0)
		v.append(1)

		k = 1

		while u[k] >= p ** (m / 2):
			q = u[k - 1] // u[k]
			u.append(u[k - 1] - q * u[k])
			v.append(v[k - 1] + q * v[k])
			k = k + 1

		print (-1) ** (k - 1) * u[k] / v[k]


restore(Z)
