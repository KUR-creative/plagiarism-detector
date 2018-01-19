#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
const int ALP = 'z'-'a' + 1;
int NOLINE = 999999999;
int vertexCount;
char p1, p2, p3;
int wgt[ALP][ALP];
int adj[ALP][ALP];
int degree[ALP];
void floyd() {
	for(int i=0; i<vertexCount; i++) {
		for(int j=0; j<vertexCount; j++) {         
			if (i == j)
				adj[i][j] = 0;
			else
				adj[i][j] = wgt[i][j];
		}
	}

	for(int k=0; k<vertexCount; k++) { // search google.
		for(int i=0; i<vertexCount; i++) {
			for(int j=0; j<vertexCount; j++) {
				if( k != i && k != j ) {
					if (adj[i][k] + adj[k][j] + degree[k] < adj[i][j]) {
						adj[i][j] = adj[i][k] + adj[k][j] + degree[k];
					}
				}
			}
		}
	}

}
int main() {
	ifstream fin ("candle.inp");
	ofstream fout("candle.out");

	fin >> vertexCount;
	fin >> p1 >> p2 >> p3;
	int findPoint1 = p1 - 'a';
	int findPoint2 = p2 - 'a';
	int findPoint3 = p3 - 'a';

	while( !fin.eof() ) {
		char vert; int row;
		fin >> vert >> row;
		int fromIndex = vert - 'a';
		degree[fromIndex] = row;

		for(int i=0; i<row; i++) {
			char toVert; int toWeight;
			fin >> toVert >> toWeight;
			
			int toIndex = toVert - 'a';
			wgt[fromIndex][toIndex] = toWeight; // 저장
		}
	} fin.close();
	for(int i=0; i<vertexCount; i++) {
		for(int j=0; j<vertexCount; j++) {
			if( wgt[i][j] == 0 ) wgt[i][j] = NOLINE; // fill_n으로 하려고 했는데 실패...
		}
	}
	floyd();

	
	for(int i=0; i<vertexCount; i++) {
		for(int j=0; j<vertexCount; j++) {
			cout.width(3); cout << adj[i][j];
		} cout << endl;
	}

	int minCost = NOLINE;
	int minIndex = 0;

	for(int i=0; i<vertexCount; i++) {
		int temp;
		if( adj[findPoint1][i] > adj[findPoint2][i] ) {
			if( adj[findPoint1][i] > adj[findPoint3][i] ) {
				temp = adj[findPoint1][i];
			} else {
				temp = adj[findPoint3][i];
			}
		} else {
			if( adj[findPoint2][i] > adj[findPoint3][i] ) {
				temp = adj[findPoint2][i];
			} else {
				temp = adj[findPoint3][i];
			}
		}
		if( temp < minCost ) {
			minCost = temp;
			minIndex = i;
		}
	}

	char DAMOIM = minIndex + 'a';
	fout << DAMOIM <<" "<< minCost<< endl;
	
	fout.close();
	return 0;
}