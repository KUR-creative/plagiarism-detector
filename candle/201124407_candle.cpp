#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;
#define INF 999999
#define MAX(A,B) ((A) > (B) ? (A) : (B))
#define MAX3(A,B,C) ((A) > (MAX(B,C)) ? (A) : (MAX(B,C)))

int N, tmpInt,tmpInt2, row, col;
char tmpChar, tmpChar2, tmpChar3;
int members[3];
bool* visitA;
bool* visitB;
bool* visitC;
int* distA;
int* distB;
int* distC;
int start, end;
int** Node;
int* degree;

int main(void) {
	ifstream fin("candle.inp");
	ofstream fout("candle.out");
	fin >> N;
	visitA = new bool[N];
	visitB = new bool[N];
	visitC = new bool[N];
	distA = new int[N];
	distB = new int[N];
	distC = new int[N];
	Node = new int*[N];
	degree = new int[N];
	for (int i = 0; i < N; i++) {
		Node[i] = new int[N];
		distA[i] = INF;
		distB[i] = INF;
		distC[i] = INF;
		visitA[i] = false;
		visitB[i] = false;
		visitC[i] = false;
		for (int j = 0; j < N; j++)
			Node[i][j] = INF;
	}
	for (int i = 0; i < 3; i++) {
		fin >> tmpChar;
		members[i] = tmpChar - 'a'; //a = 0 ~ z = 25 까지 숫자
		//cout << members[i] << endl;
	}
	for (int i = 0; i < N; i++) {
		fin >> tmpChar >> tmpInt;
		row = tmpChar - 'a';
		degree[row] = tmpInt;
		for (int j = 0; j < tmpInt; j++) {
			fin >> tmpChar2 >> tmpInt2;
			col = tmpChar2 - 'a';
			Node[row][col] = tmpInt2;
			//cout << tmpChar << ", " << tmpChar2 << " = " << Node[row][col] << "  <>  ";
		}
		//cout << endl;
	}
	int min, v;

	//A

	for (int j = 0; j < N; j++){
		if (Node[members[0]][j] != INF){
			distA[j] = Node[members[0]][j];
		}
	}
	distA[members[0]] = 0;        // 시작점의(자기자신) 거리 0

	for (int i = 0; i < N; i++) {
		min = INF;
		for (int j = 0; j < N; j++) {
			if (visitA[j] == false && min > distA[j]) {    // 무한대가 아닌 정점 중, 방문하지 않은 곳
				min = distA[j]; //최소값 변경
				v = j; //해당 index
			}
		}
		visitA[v] = true;   // 가장 가까운 정점으로 방문, i정점에서 가장 가까운 최단경로 v
		for (int j = 0; j < N; j++){
			if (distA[j] > distA[v] + Node[v][j] + degree[v])       // 방문한 정점을 통해 다른 정점까지의 거리가 짧아지는지 계산하여 누적된값 저장
				distA[j] = distA[v] + Node[v][j] + degree[v];
		}
	}

	//B

	for (int j = 0; j < N; j++) {
		if (Node[members[1]][j] != INF) {
			distB[j] = Node[members[1]][j];
		}
	}
	distB[members[1]] = 0;        // 시작점의(자기자신) 거리 0


	for (int i = 0; i < N; i++) {
		min = INF;
		for (int j = 0; j < N; j++) {
			if (visitB[j] == false && min > distB[j]) {    // 무한대가 아닌 정점 중, 방문하지 않은 곳
				min = distB[j]; //최소값 변경
				v = j; //해당 index
			}
		}
		visitB[v] = true;   // 가장 가까운 정점으로 방문, i정점에서 가장 가까운 최단경로 v
		for (int j = 0; j < N; j++) {
			if (distB[j] > distB[v] + Node[v][j] + degree[v])       // 방문한 정점을 통해 다른 정점까지의 거리가 짧아지는지 계산하여 누적된값 저장
				distB[j] = distB[v] + Node[v][j] + degree[v];
		}
	}

	//C

	for (int j = 0; j < N; j++) {
		if (Node[members[2]][j] != INF) {
			distC[j] = Node[members[2]][j];
		}
	}
	distC[members[2]] = 0;        // 시작점의(자기자신) 거리 0

	for (int i = 0; i < N; i++) {
		min = INF;
		for (int j = 0; j < N; j++) {
			if (visitC[j] == false && min > distC[j]) {    // 무한대가 아닌 정점 중, 방문하지 않은 곳
				min = distC[j]; //최소값 변경
				v = j; //해당 index
			}
		}
		visitC[v] = true;   // 가장 가까운 정점으로 방문, i정점에서 가장 가까운 최단경로 v
		for (int j = 0; j < N; j++) {
			if (distC[j] > distC[v] + Node[v][j] + degree[v])       // 방문한 정점을 통해 다른 정점까지의 거리가 짧아지는지 계산하여 누적된값 저장
				distC[j] = distC[v] + Node[v][j] + degree[v];
		}
	}

	//cout << "------------------------------" << endl;

	//for (int i = 0; i < N; i++) {
	//	cout << distA[i] << endl;
	//}

	//cout << "------------------------------" << endl;

	//for (int i = 0; i < N; i++) {
	//	cout << distB[i] << endl;
	//}
	//cout << "------------------------------" << endl;

	//for (int i = 0; i < N; i++) {
	//	cout << distC[i] << endl;
	//}

	//cout << "------------------------------" << endl;

	int Index = -1;
	int MinTime = INF;

	for (int i = 0; i < N; i++) {
		int temp = MAX3(distA[i], distB[i], distC[i]);
		//cout << temp << endl;
		if (MinTime > temp) {
			Index = i;
			MinTime = temp;
		}
		if (MinTime == temp) {
			if (MAX(Index, i) == Index) { //크면 바뀐다
				MinTime = temp;
				Index = i;
			}
		}
	}
	char result = Index + 'a';
	fout << result << " " << MinTime;

	return 0;
}