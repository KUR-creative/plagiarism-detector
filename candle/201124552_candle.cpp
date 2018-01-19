#include <map>
#include <math.h>
#include <stack>
#include <iostream>
#include <queue>
#include <fstream>
#include <cstdio>

#define INF 99999
#pragma warning(disable: 4996)
using namespace std;

stack <int> st;
priority_queue <int> pq;

int N, p, edge[26][26], index[26], value[26], path[26][26], 
	visit[3][26], dist[3][26], degree[26], maxDist[26],
	min_dist = INF, idx = 0;
char meet_V, start[3];

typedef struct {
	char name;
	char connected[26];
	int degree;
	int connectcost[26];
}graphINFO;


int max(int a, int b) {
	if (a > b) return a;
	else return b;
}

/////////referenced by taejin kim ///////////
void dijkstra(int s, int idx) {

	int v, min_D, temp = degree[s]; //첫 degree 제외
	degree[s] = 0;
	dist[idx][s] = 0;
	
	for (int i = 0; i < N; i++) {
		min_D = INF;
		if (min_D == INF) {
			for (int j = 0; j < N; j++) {
				if (visit[idx][j] == 0 && min_D > dist[idx][j]) { 
					min_D = dist[idx][j];
					v = j;
				}
			}
		}
		visit[idx][v] = 1; //방문 check
		//modified dijkstra algorithm
		for (int k = 0; k < N; k++) {
			int compare = dist[idx][v] + edge[v][k];
			if (i == 0 && (dist[idx][k] > compare)) dist[idx][k] = dist[idx][v] + edge[v][k] + degree[v];			
			else if (i != 0 && dist[idx][k] > compare+ degree[v]) dist[idx][k] = compare + degree[v];			
		}
	}
	degree[s] = temp;
}



int main() {

	stack <int> st;
	priority_queue <int> pq;
	ifstream fin("candle.inp");
	ofstream fout("candle.out");
	graphINFO graph[26];


	fin >> N;
	for (int i = 0; i < 3; i++)  fin >> start[i];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)	edge[i][j] = INF;
		value[i] = INF;
	}

	for (int i = 0; i < N; i++) {
		fin >> graph[i].name >> graph[i].degree;
		for (int j = 0; j < graph[i].degree; j++) {
			fin >> graph[i].connected[j] >> graph[i].connectcost[j];
			edge[graph[i].name - 97][graph[i].connected[j] - 97] = graph[i].connectcost[j];
			degree[graph[i].name - 97] = graph[i].degree;
		}
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)  
			path[i][j] = INF;

	for (int i = 0; i < N; i++) {
		int vIdx = 0, dN = 0;
		for (int j = 0; j < 3; j++) dist[j][i] = INF;

		if (i <= N) {
			fin >> vIdx >>dN;			
			vIdx -= 97;
			degree[vIdx] = dN;
		}

		if (degree[vIdx] == dN) {
			for (int j = 0; j < dN; j++) {
				int connectedV = 0, connectedE = 0; //tmp 
				fin >> connectedV >> connectedE;
				connectedV -= 97;
				path[vIdx][connectedV] = connectedE;
			}
		}
	}

	while (idx < 3) { 
		dijkstra(start[idx]-97, idx);
		idx++; 
	}

	//MIN COST CALC//
	for (int j = 0; j < N; j++) {
		if (j < N) {
			int distTemp = max(dist[0][j], max(dist[1][j], dist[2][j]));
			if (min_dist > distTemp) {
				min_dist = distTemp;  
				meet_V = (char)(j + 97);
			}
			else continue;
		}
	}
	fout << meet_V <<" " << min_dist ;

	return 0;
}