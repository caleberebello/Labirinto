#include<stdio.h>
#include<stdlib.h>
#include <time.h>
#define MAX 10


void imprimeLabirinto(int M[MAX][MAX], int n, int m) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			if (M[i][j] == -2){
				printf("|  |");
			}
			if (M[i][j] == -1){
				printf("|00|");
			}
			if (M[i][j] >= 0) {
				printf("|%02d|", M[i][j]);
				//printf("|00|");
			}
		}
		printf("\n");
	}
}

void obtemLabirinto(int M[MAX][MAX], int *n, int *m,int *Li, int *Ci, int *Lf, int *Cf) {
	int i, j, d;
//	/*scanf("%d %d", n, m); /* dimensoes do labirinto */
//	scanf("%d %d", Li, Ci); /* coordenadas da posicao inicial */
//	scanf("%d %d", Lf, Cf); /* coordeandas da posicao final (saida) */
	/* labirinto: 1 = parede ou obstaculo
	 0 = posicao livre */
 	srand(time(NULL));
	for (i = 0; i < *n; i++){
		for (j = 0; j < *m; j++) {
		   	d = (rand() % 1000);
		   	//printf("d = %d",d);
			if (d == 1){
			   	M[i][j] = -2;
			}
			else{
				M[i][j] = -1;
			}
		}
	}
}

int labirinto(int M[MAX][MAX], int deltaL[], int deltaC[],int Li, int Ci, int Lf, int Cf) {
	int L, C, k, passos;
	printf("Li = %d, Ci = %d, Lf = %d, Cf = %d\n",Li,Ci,Lf,Cf);
	if ((Li == Lf) && (Ci == Cf)){
		printf("M[Li][Ci] = %d\n",M[Li][Ci]);
		return M[Li][Ci];
		/* testa todos os movimentos a partir da posicao atual */
	}
	for (k = 0; k < 4; k++) {
		L = Li + deltaL[k];
		C = Ci + deltaC[k];
	//8	printf("--->L = %d, deltaL = %d, C = %d, deltaC = %d\n",L,deltaL[k],C,deltaC[k]);
	/* verifica se o movimento eh valido e gera uma solucao factivel */
		if (M[L][C] == -1) { // nao visitou ainda
			M[L][C] = M[Li][Ci] + 1;
			passos = labirinto(M, deltaL, deltaC, L, C, Lf, Cf);
			if (passos > 0){
				return passos;
			}
		}

	}
	return 0;
}

int main() {
	int M[MAX][MAX], resposta, n=10, m=10, Li=1, Ci=1, Lf=8, Cf=8,k,l;
	printf("n = %d,m = %d, Li= %d, Ci = %d, Lf = %d, Cf = %d, ",n,m,Li,Ci,Lf,Cf);
	/* define os movimentos validos no labirinto */
	int deltaL[4] = { 0, +1, 0, -1}; //possiveis posicoes em linha
	int deltaC[4] = {+1, 0, -1, 0};  // 			coluna
	/* obtem as informacoes do labirinto */
	
//	obtemLabirinto(M, &n, &m, &Li, &Ci, &Lf, &Cf);
	int i, j, d;
/* n,m dimensoes do labirinto */
/* Li,Ci coordenadas da posicao inicial */
/* Lf, Cf coordeandas da posicao final (saida) */
	/* labirinto: 1 = parede ou obstaculo
	 0 = posicao livre */
 	srand(time(NULL));
	for (i = 0; i < n; i++){
		for (j = 0; j < m; j++) {
			if((i==0)||(i==9)||(j==0)||(j==9)){
				M[i][j] = -2;
			}
			else{
		   		d = (rand() % 3);
		   		//printf("d = %d",d);
				if (d == 1){
			   		M[i][j] = -2;
				}
				else{
					M[i][j] = -1;
				
				}
			}
		}
	}
	printf("\n");
	for(k=0;k<MAX;k++){
		for(l=0;l<MAX;l++){
			printf("%d",M[k][l]);
		}
		printf("\n");
	}

//	M[Li - 1][Ci - 1] = 0; /* define a posicao inicial no tabuleiro */


	/* tenta encontrar um caminho no labirinto */
	resposta = labirinto(M, deltaL, deltaC, Li, Ci, Lf, Cf);
	printf("resposta %d\n",resposta);
	if ((resposta == 0)||(M[Li][Ci]== -2)){
		printf("Nao existe solucao.\n");
		imprimeLabirinto(M, n, m);
	}
	else {
		printf("Existe uma solucao em %d passos.\n", resposta);
		imprimeLabirinto(M, n, m);
	}

return 0;

}