def volta(matriz, atual, posterior):
	for i in range(9):
		for j in range(9):
			if matriz[i][j+1] == 0:
				posterior = atual
			elif matriz[i+1][j] == 0:
				posterior = atual
			elif matriz[i][j-1] == 0:
				posterior = atual
			elif matriz[i-1][j] == 0:
				posterior = atual

def movimenta(matriz, posterior, atual):
	atual = matriz[0][0]
	while(atual != matriz[9][9]):
		for i in range(9):
			for j in range(9):
				if matriz[i][j+1] == 1:
					posterior = matriz[i][j]
					atual = posterior
				elif matriz[i+1][j] == 1:
					posterior = matriz[i][j]
					atual = posterior
				elif matriz[i][j-1] == 1:
					posterior = matriz[i][j]
					atual = posterior
				elif matriz[i-1][j] == 1:
					posterior = matriz[i][j]
					atual = posterior
				else:
					volta(matriz, atual, posterior)
