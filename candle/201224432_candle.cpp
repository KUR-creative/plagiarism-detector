#include <iostream>
#include <fstream>
using namespace std;

#define MAXNUM 0xffffff

char node[3];
int table[26][26];
int degree[26];

int main(){

	ifstream inFile("candle.inp");
	ofstream outFile("candle.out");

	int inputNum;
	int index = 0; //index
	int tempD; //임시degree 저장 장소
	int minimumPath; //최소경로 변수
	char result;

	inFile >> inputNum
		   >> node[0]  >> node[1] >> node[2] ;

	char inputCha, tempChar;
	

	for(int i = 0; i < inputNum; i++){

		inFile >> inputCha;
		inFile >> tempD;
		degree[inputCha - 97] = tempD;
		for(int j = 0; j < tempD; j++){
			
			inFile >> tempChar;
			inFile >> table[inputCha-97][tempChar - 97];
		}
	}

	///////////플로이드 워셜/////
	for (int i = 0; i < inputNum; i++) {
		for (int j = 0; j < inputNum; j++) {
			if(i == j) continue;
			if (table[i][j] == 0) table[i][j] = MAXNUM;
			else table[i][j] += degree[j];
		}
	}

	for (int k = 0; k < inputNum; k++) {
		for (int i = 0; i < inputNum; i++) {
			for (int j = 0; j < inputNum; j++) {
				if (table[i][j] > table[i][k] + table[k][j]) {
					table[i][j] = table[i][k] + table[k][j];
				}
			}
		}
	}
	////////////////////////////


	minimumPath = MAXNUM;
	int temp;
	for(int i = 0; i < inputNum; i++){
		temp = 0;
		for(int j = 0; j < 3; j++){
			if(temp < table[node[j]-97][i] - degree[i])
				temp = table[node[j]-97][i] - degree[i];
		}
		if(minimumPath > temp){
			minimumPath = temp;
			index = i;
		}
	}
	//결과 출력
	result = (char)(index + 97);
	outFile << result << " " << minimumPath << endl;
	return 0;
}