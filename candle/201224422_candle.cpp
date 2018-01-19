#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"

#define infinity 99999
FILE *fd;
FILE *fd1;
int weight[27];
int shortest[26][26];

int max_3(int a, int b, int c) {
	if (a >= b && a >= c)return a;
	else if (b >= c&&b >= a)return b;
	else return c;
}
int check(char c) {
	if (c == 'a')return 0;
	else if (c == 'b')return 1;
	else if (c == 'c')return 2;
	else if (c == 'd')return 3;
	else if (c == 'e')return 4;
	else if (c == 'f')return 5;
	else if (c == 'g')return 6;
	else if (c == 'h')return 7;
	else if (c == 'i')return 8;
	else if (c == 'j')return 9;
	else if (c == 'k')return 10;
	else if (c == 'l')return 11;
	else if (c == 'm')return 12;
	else if (c == 'n')return 13;
	else if (c == 'o')return 14;
	else if (c == 'p')return 15;
	else if (c == 'q')return 16;
	else if (c == 'r')return 17;
	else if (c == 's')return 18;
	else if (c == 't')return 19;
	else if (c == 'u')return 20;
	else if (c == 'v')return 21;
	else if (c == 'w')return 22;
	else if (c == 'x')return 23;
	else if (c == 'y')return 24;
	else if (c == 'z')return 25;
}
char check2(int a) {
	if (a == 0)return 'a';
	else if (a == 1)return 'b';
	else if (a == 2)return 'c';
	else if (a == 3)return 'd';
	else if (a == 4)return 'e';
	else if (a == 5)return 'f';
	else if (a == 6)return 'g';
	else if (a == 7)return 'h';
	else if (a == 8)return 'i';
	else if (a == 9)return 'j';
	else if (a == 10)return 'k';
	else if (a == 11)return 'l';
	else if (a == 12)return 'm';
	else if (a == 13)return 'n';
	else if (a == 14)return 'o';
	else if (a == 15)return 'p';
	else if (a == 16)return 'q';
	else if (a == 17)return 'r';
	else if (a == 18)return 's';
	else if (a == 19)return 't';
	else if (a == 20)return 'u';
	else if (a == 21)return 'v';
	else if (a == 22)return 'w';
	else if (a == 23)return 'x';
	else if (a == 24)return 'y';
	else if (a == 25)return 'z';
}
void dij(int n, int v, int cost[27][27], int dist[],int weight[]){
	int i, u, count, w, flag[27], min;
	for (i = 1; i <= n; i++)
		flag[i] = 0, dist[i] = cost[v][i];
	count = 2;
	while (count <= n){
		min = 99999;
		for (w = 1; w <= n; w++)
			if (dist[w]<min && !flag[w])
				min = dist[w] , u = w;
		flag[u] = 1;
		count++;  
		for (w = 1; w <= n; w++)
			if ((dist[u] + cost[u][w] + weight[u-1] < dist[w]) && !flag[w])
				dist[w] = dist[u] + cost[u][w] + weight[u-1];
	}
}

int main(){
	int n, v, i, j, cost[27][27], dist[27];
	int totalvertex;
	int minicost;
	char minivertex;
	int tempint, tempint1;
	char tempchar[2], tempchar1[2];
	char first[2], second[2], third[2];
	fd = fopen("candle.inp", "r");
	fd1 = fopen("candle.out", "w");
	fscanf(fd, "%d", &totalvertex);
	fscanf(fd, "%s %s %s", &first, &second, &third);
	for (int i = 0; i < 27; i++) {
		for (int k = 0; k < 27; k++) {
			if(i==0||k==0)	cost[i][k] = 0;
			else cost[i][k] = infinity;
		}
	}
	for (int i = 0; i < 26; i++) {
		for (int k = 0; k < 26; k++) {
			 shortest[i][k] = infinity;
		}
	}

	for (int i = 0; i < totalvertex; i++) {
		fscanf(fd, "%s", &tempchar);
		fscanf(fd, "%d", &tempint);
		weight[check(tempchar[0])] = tempint;
		for (int k = 0; k < tempint; k++) {
			fscanf(fd, "%s", &tempchar1);
			fscanf(fd, "%d", &tempint1);
			cost[check(tempchar[0])+1][check(tempchar1[0])+1] = tempint1;
			if (cost[i+1][k+1] == 0) cost[i+1][k+1] = infinity;
		}
	}
/*	for (int i = 0; i < totalvertex; i++) {
		printf("%d \n", weight[i]);
	}*/
//	printf("\n Enter the number of nodes:");
//	scanf("%d", &n);
	n = 26;
	for (int v = 1; v < totalvertex+1; v++) {
		dij(n, v, cost, dist, weight);
		for (int i = 1; i < 27; i++) {
			if(v==i)shortest[v - 1][i - 1] = 0;
			else shortest[v - 1][i - 1] = dist[i];
		}
	}
/*	printf("\n Enter the cost matrix:\n");
	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
		{
			cost[i][j] = 1;
			//scanf("%d", &cost[i][j]);
			if (cost[i][j] == 0)
				cost[i][j] = infinity;
		}*/
//	for (int i = 0; i < 27; i++) {
//		for (int k = 0; k < 27; k++) {
//			printf("%d ", cost[i][k]);
//		}
//	}

/*	for (int i = 0; i < 10; i++) {
		for (int k = 0; k < 10; k++) {
			printf("%d ", shortest[i][k]);
		}
		printf("\n");
	}*/
	int good;
//	printf("%d    %d    %d   %s   %s   %s\n", check(first[0]), check(second[0]), check(third[0]),first,second,third);
	minicost = 99999;
	for (int i = 0; i < totalvertex; i++) {
		if (minicost > max_3(shortest[check(first[0])][i], shortest[check(second[0])][i], shortest[check(third[0])][i]))  {
			minicost = max_3(shortest[check(first[0])][i], shortest[check(second[0])][i], shortest[check(third[0])][i]);
			good = i;
		}
	}
	fprintf(fd1,"%c %d",check2(good) ,minicost);
/*  printf("\n Enter the source matrix:");
	scanf("%d", &v);
	dij(n, v, cost, dist,weight);

	
	printf("\n Shortest path:\n");
	for (i = 1; i <= n; i++)
		if (i != v)
			printf("%d->%d,cost=%d\n", v, i, dist[i]);*/
	return 0;
}