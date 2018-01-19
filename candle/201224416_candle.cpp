#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;
 
int map[26][26];
int vD[26];
char friends[3];
 
int mapCount;
 
void floydWarshall() {
	for (int i = 0; i < mapCount; i++) {
		for (int j = 0; j < mapCount; j++) {
			for (int k = 0; k < mapCount; k++) {
				if (map[k][j] > map[k][i] + map[i][j] + vD[i]) {
					map[k][j] = map[k][i] + map[i][j] + vD[i];
					//courseVector.at(k * nodeNum + j) = courseVector.at(i * nodeNum + j);
				}
			}
		}
	}
}

int main() {
	ifstream fin;
	ofstream fout;
 
	fin.open("candle.inp");
	//fout.open("candle.out");
	FILE *fp = fopen("candle.out", "w");
 
	fin >> mapCount;
 
	fin >> friends[0] >> friends[1] >> friends[2];
	friends[0] -= 97;
	friends[1] -= 97;
	friends[2] -= 97;
 
	for (int i = 0; i < mapCount; i++) {
		for (int j = 0; j < mapCount; j++) {
			map[i][j] = 99999;
		}
	}
 
	char tempAlpabet1;
	int tempNum1;
	char tempAlpabet2;
	int tempNum2;
 
	for (int i = 0; i < mapCount; i++) {
		
		fin >> tempAlpabet1;
		fin >> tempNum1;
		vD[tempAlpabet1-97] = tempNum1;
		for (int j = 0; j < tempNum1; j++) {
			fin >> tempAlpabet2;
			fin >> tempNum2;
 
			map[tempAlpabet1 - 97][tempAlpabet2 - 97] = tempNum2;
		}
 
	}
 
	floydWarshall();

	int minDist = 99999;
	char result = 0;
	for(int i = 0 ; i < mapCount ; i++){
		if(minDist > max(max(map[friends[0]][i],map[friends[1]][i]),map[friends[2]][i])){
			minDist = max(max(map[friends[0]][i],map[friends[1]][i]),map[friends[2]][i]);
			result = i;
		}
	}

	for (int i = 0; i < mapCount; i++) {
		for (int j = 0; j < mapCount; j++) {
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	fprintf(fp,"%c %d",result+97,minDist);
	//cout << (char)(result+97) << " " << minDist << endl;
}
 
