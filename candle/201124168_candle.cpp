#include <iostream>
#include <fstream>
#include <algorithm>
#define MAX 26
#define END 0
#define PASS 1
#define INT(X) ((int)((X)-'a'))
#define INPUT "candle.inp"
#define OUTPUT "candle.out"

using namespace std;

struct { int x, y, degree; } node[MAX];

int distDP[MAX][MAX][2];

char start[3], result;
int N, minT;

void doFloyd() {
    // Do Floyd-Warshall Algorithm
    for (int k = 0 ; k < N ; ++k)
        for (int i = 0 ; i < N ; ++i)
            for (int j = 0 ; j < N ; ++j)
                if (distDP[i][j][END] > distDP[i][k][PASS] + distDP[k][j][END]) {
                    distDP[i][j][END] = distDP[i][k][PASS] + distDP[k][j][END];
                    distDP[i][j][PASS] = distDP[i][j][END] + node[j].degree;
                }

    minT = 1000000;

    for(int k = 0 ; k < N ; ++k) {
        int alt = 0;
        for(int i = 0 ; i < 3 ; ++i) { alt = max(alt, distDP[INT(start[i])][k][END]); }
        if(alt < minT) {
            result = k + 'a';
            minT = alt;
        }
    }
}

int main() {
    ifstream inpStream(INPUT) ;
	ofstream outStream(OUTPUT) ;

	// input
    inpStream >> N;
    for(int i = 0 ; i < 3 ; ++i) { inpStream >> start[i]; }
    char src, dest;
    int n, w;
	for(int i = 0 ; i < N ; ++i) {
        inpStream >> src >> n;
        node[INT(src)].degree = n;
        for(int j = 0 ; j < n ; ++j) {
            inpStream >> dest >> w;
            distDP[INT(src)][INT(dest)][END] = w;
        }
	}

	// init
    for(int i = 0 ; i < N ; ++i)
        for(int j = 0; j < N ; ++j) {
            if(i == j) { continue; }
            if(distDP[i][j][END] == 0) { distDP[i][j][END] = distDP[i][j][PASS] = 1000000; }
            distDP[i][j][PASS] = distDP[i][j][END] + node[j].degree;
        }

	doFloyd();

    // output
    outStream << result << " " << minT << endl;

	return 0;
}
