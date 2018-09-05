#Calebe Roberto
#Paulo Marinho
#Nickso Calheiros
from random import *

#função para criar o labirinto
def criar_matriz(m,n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            r = randint(0,1)
            linha.append(r)
        matriz.append(linha)
    matriz[0][0] = 0
    matriz[9][9] = 0
    return matriz

#verificar movimentações
def labirinto(matriz, movL, movC, Li, Lf, Ci, Cf):
    passos = 0
    if Li == Lf and Ci == Cf:
        passos = passos + 1
        matriz[Li][Ci] = 9
        return matriz[Li][Ci]

    for i in range(4):
        L = Li + movL[i]
        C = Ci + movC[i]
        if matriz[L][C] == 0:
            matriz[L][C] = matriz[Li][Ci] + 1
            passos = labirinto(matriz, movL, movC, Li, Lf, Ci, Cf)
            if passos > 0:
                return passos
    return 0

#main
m, n = 10, 10
Li, Ci, Lf, Cf = 0, 0, 9, 9
lab = criar_matriz(m,n)
movL = [0, +1, 0, -1]
movC = [+1, 0, -1, 0]
resposta = labirinto(lab, movL, movC, Li, Lf, Ci, Cf)

if resposta == 0:
    print("Não existe solução")
    for i in range(10):
        print(lab[i])

else:
    print("Existe uma solução em %d passos" % resposta)
    for i in range(10):
        print(lab[i])
