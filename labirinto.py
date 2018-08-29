from random import *

lista = []

def criar_matriz(m,n):
	matriz = []
	for i in range(m):
		linha = []
		for i in range(n):
			r = randint(0,1)
			linha.append(r)
		matriz.append(linha)
	return matriz

def empilha(lista, posterior):
	lista.append(posterior)
	print(lista)

#def desempilha(lista, posterior):
#	lista.pop(posterior)
	
def movimenta(matriz):
	atual = matriz[0][0]
	while(atual != matriz[9][9]):
		for i in range(9):
			for j in range(9):
				if matriz[i][j] == 0:
					matriz[i][j] = "x"
					#empilha(lista)
				elif matriz[i+1][j] == 0:
					matriz[i][j] = "x"
					#empilha(lista)
				elif matriz[i][j-1] == 0:
					matriz[i][j] = "x"
					#empilha(lista)
				elif matriz[i-1][j] == 0:
					matriz[i][j] = "x"
					#empilha(lista)
				else:
					volta(matriz)					
		return matriz

def volta(matriz):
	atual = 0
	posterior = 0
	for i in range(9):
		for j in range(9):
			if matriz[i][j+1] == 1:
				posterior = atual
				#desempilha(lista, posterior)
			elif matriz[i+1][j] == 1:
				posterior = atual
				#desempilha(lista, posterior)
			elif matriz[i][j-1] == 1:
				posterior = atual
				#desempilha(lista, posterior)
			elif matriz[i-1][j] == 1:
				posterior = atual
				#desempilha(lista, posterior)

m = 10
n = 10
labirinto = criar_matriz(m,n)
print(movimenta(labirinto))
