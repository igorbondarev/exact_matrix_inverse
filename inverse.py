from sympy import Matrix, pprint

p   = 5
m   = 10

mat = [ [4, 1, 1],
	[1, 4, 1],
	[1, 1, 4] ]

dimension = len(mat)

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
		
mod_matrix = matrix_by_mod(mat, p)

A = Matrix(mod_matrix)
A_inv = A.inv_mod(5)
new_mat = [[A_inv[y, x] for x in range(len(mat))] for y in range(len(mat))]

def calc_vec_z(vec_b):

	bk =  [0 for x in range(m + 1)]
	bkp = [0 for x in range(m + 1)]
	xkp = [0 for x in range(m + 1)]
	Matrix_Cp = Matrix(new_mat)
	Matrix_A = Matrix(mat)
	bk[0] = Matrix(vec_b)

	Z_vec =  [0 for x in range(dimension)]
	Z = Matrix(Z_vec)

	for k in range(m):
		bkp[k] = vec_by_mod(bk[k], p)
		xkp[k] = vec_by_mod(Matrix_Cp * bkp[k], p)
		bk[k + 1] = (bk[k] - Matrix_A * xkp[k]) / p

	for k in range(m):
		Z = Z + (p ** k) * xkp[k]

	return Z

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
	print "****"

for d in range(len(mat)):
	local_b = [(0 + (x == d)) for x in range(len(mat))]
	Z_vec = calc_vec_z(local_b)
	restore(Z_vec)
