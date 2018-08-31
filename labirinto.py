from random import *

lista = []

def criar_matriz(m,n):
	matriz = []
	for i in range(m):
		linha = []
		for j in range(n):
			r = randint(0,1)
			linha.append(r)
			if r == 1:
				matriz[i][j] = -2
			else:
				matriz[i][j] = -1
		matriz.append(linha)
	return matriz

def labirinto(matriz,deltaL,deltaC,Li,Ci,Lf,Cf):
	if((Li == Lf) and (Ci == Cf)):
		return matriz[Li][Ci]

	for i in range(4):
		L = Li + deltaL[i]
		C = Ci + deltaC[i]
		if matriz[L][C] == -1:
			matriz[L][C] = matriz[Li][Ci] + 1
			caminho = labirinto(matriz, deltaL, deltaC, L, C, Lf, Cf)
			if caminho > 0:
				return caminho

m = 10
n = 10
deltaL = [0, +1, 0, -1]
deltaC = [+1, 0, -1, 0]
