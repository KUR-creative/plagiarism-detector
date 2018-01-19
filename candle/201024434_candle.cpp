#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define pii pair<int, int>
#define INF 9999999

int n; 
int v1, v2, v3;
int t;
char place;

vector<vector<int> > adj_mat(26, vector<int>(26)); 
vector<int> degree(26, 0);

void init(vector<vector<int> >& mat);

void input(istream& pin) {
	char c1, c2, c3;
	init(adj_mat);
	pin >> n;
	pin >> c1 >> c2 >> c3;

	v1 = c1 - 'a';
	v2 = c2 - 'a';
	v3 = c3 - 'a';
	for(int i=0; i<n; i++) {
		char src;
		int num;
		pin >> src >> num;
		degree[src-'a'] = num;

		for(int j=0; j<num; j++) {
			char dst;
			int weight;
			pin >> dst >> weight;
			adj_mat[src-'a'][dst-'a'] = weight;
		}
	}
}

void init(vector<vector<int> >& mat) {
	for(int i=0; i<26; i++) {
		for(int j=0; j<26; j++) {
			if(i==j) mat[i][j] = 0;
			else 
				mat[i][j] = INF;
		}
	}
}

void method() {
	for(int k=0; k<n; k++) {
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				
				if(i == k || j == k) {
					if(adj_mat[i][j] > adj_mat[i][k] + adj_mat[k][j])  
						adj_mat[i][j] = adj_mat[i][k] + adj_mat[k][j];
				}
				else if(adj_mat[i][j] > adj_mat[i][k] + adj_mat[k][j] + degree[k]) { 
						adj_mat[i][j] = adj_mat[i][k] + adj_mat[k][j] + degree[k];
				}
			}
		}
	}
}

void getSolution() {
	t = INF;
	place;
	for(int i=0; i<26; i++) {
		int dist = max({adj_mat[v1][i], adj_mat[v2][i], adj_mat[v3][i]}) ;
		if(dist < t) {
			t = dist;	
			place = (char)('a' + i);
		}
	}



}

int main() {
	ifstream fin("candle.inp");
	ofstream fout("candle.out");	
	input(fin);
	method();
	/*
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(adj_mat[i][j] > 1234) 
				cout << "INF" << " ";
			else 
			cout << adj_mat[i][j] << " ";
		}
		cout << endl;
	}
	*/
	getSolution();
	fout << place << " " << t;
	return 0;
}
