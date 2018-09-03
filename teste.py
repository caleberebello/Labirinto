from random import *

def criar_matriz(m,n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            r = randint(0,1)
            if r == 1:
                matriz[i][j] = -2
            else:
                matriz[i][j] = -1
            linha.append(r)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz, m, n):
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == -2:
                print("|XX|")
            if matriz[i][j] == -1:
                print("|00|")
            if matriz[i][j] >= 0:
                print("%02d" % matriz[i][j])
    return matriz
                
def labirinto(matriz, deltaL, deltaC, Li, Lf, Ci, Cf):
    if Li == Lf and Ci == Cf:
        return matriz[Li][Ci]

    for i in range(4):
        L = Li + deltaL[i]
        C = Ci + deltaC[i]
        if matriz[L][C] == -1:
            matriz[L][C] = matriz[Li][Ci] + 1
            passos = labirinto(matriz[L][C], deltaL, deltaC, Li, Lf, Ci, Cf)
            if passos > 0:
                return passos
    
m = 10
n = 10
Li=0
Ci=0
Lf=9
Cf=9
lab = criar_matriz(m,n)
deltaL = [0, +1, 0, -1]
deltaC = [+1, 0, -1, 0]
resposta = labirinto(lab, deltaL, deltaC, Li, Lf, Ci, Cf)

if resposta == 0:
    print("Não existe solução")
else:
    print("Existe uma solução em %d passos" % resposta)
    imprimir_matriz(lab, m, n)
