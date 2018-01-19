#include <iostream>
#include <cstdio>
#include <fstream>
#include <string.h>
#include <algorithm>
using namespace std;

#define INF 99999

void path();

int G[27][27];
int degree[27];
int N;

int main(){
	ifstream in("candle.inp");
	ofstream out("candle.out");

	char f1, f2, f3;
	in >> N >> f1 >> f2 >> f3;

	for(int i = 1; i <= N; i++)
		for(int j = 1; j <= N; j++)
			G[i][j] = INF;
	
	for(int i = 0; i < N; i++){
		char vStart;
		int n;

		in >> vStart >> n;
		degree[vStart-0x60] = n;
		for(int j = 0; j < n; j++){
			char vEnd;
			int d;
			in >> vEnd >> d;
			G[vStart-0x60][vEnd-0x60] = d;
		}
	}

	path();

	int a = f1-0x60;
	int b = f2-0x60;
	int c = f3-0x60;

	int node, dist = INF;

	for(int i = 1; i <= N; i++){
		if(dist > max(G[a][i], max(G[b][i], G[c][i]))){
			dist = max(G[a][i], max(G[b][i], G[c][i]));
			node = i;
		}
	}

	out << (char)(node + 0x60) << " " << dist << endl;
	
	return 0;
}

void path(){
	for(int k = 1; k <= N; k++){
		for(int i = 1; i <= N; i++){
			for(int j = 1; j <= N; j++){
				if(G[i][j] > G[i][k] + G[k][j] + degree[k]){
					G[i][j] = G[i][k] + G[k][j] + degree[k];
				}
			}
		}
	}
}