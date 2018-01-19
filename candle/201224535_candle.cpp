#include <iostream>
#include <cstdio>
#include <fstream>
#include <string.h>
#include <algorithm>
using namespace std;

int input[27][27];
int degree[27];
int N;
char friend_1, friend_2, friend_3;
int result, dist = 99999;

int main(){
	ifstream fin;
	fin.open("candle.inp");
	ofstream fout;
	fout.open("candle.out");



	fin >> N >> friend_1 >> friend_2 >> friend_3;

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			input[i][j] = 99999;
		}
	}


	for (int i = 0; i < N; i++){
		char start_vertax;
		int connect_edge_num;

		fin >> start_vertax >> connect_edge_num;
		degree[start_vertax - 0x61] = connect_edge_num;
		for (int j = 0; j < connect_edge_num; j++){
			char connected_vertax;
			int length;
			fin >> connected_vertax >> length;
			input[start_vertax - 0x61][connected_vertax - 0x61] = length;
		}
	}
	//여기까지가 input을 2차원 배열로 구성

	for (int k = 0; k < N; k++){
		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++){
				if (input[i][j] > input[i][k] + input[k][j] + degree[k]){
					input[i][j] = input[i][k] + input[k][j] + degree[k];
				}
			}
		}
	}

	int a = friend_1 - 0x61;
	int b = friend_2 - 0x61;
	int c = friend_3 - 0x61;



	for (int i = 0; i < N; i++){
		if (dist > max(input[a][i], max(input[b][i], input[c][i]))){
			dist = max(input[a][i], max(input[b][i], input[c][i]));
			result = i;
		}
	}

	fout << (char)(result + 0x61) << " " << dist << endl;

	return 0;
}

