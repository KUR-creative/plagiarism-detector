#include <iostream>
#include <fstream>
using namespace std;
int num_node;
char place_friend[3];
int dist[26][26];
int degree[26];
int answer=0;
int min_path=9999;
void calculate();
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("candle.inp");
	fout.open("candle.out");
	fin>>num_node;

	for(int i=0;i<3;i++)
		fin>>place_friend[i];
	for(int i=0;i<num_node;i++){
		char x;
		int y;
		char z;
		fin>>x>>y;
		degree[x-'a']=y;
		for(int j=0;j<y;j++){
			fin>>z;
			fin>>dist[x-'a'][z-'a'];
		}
	}
	calculate();
	for(int i=0;i<num_node;i++){
		int temp=0;
		for(int j=0;j<3;j++){
			if(temp<dist[place_friend[j]-'a'][i]-degree[i])
				temp=dist[place_friend[j]-'a'][i]-degree[i];
			else
				;
		}
		if(min_path>temp){
			min_path=temp;
			answer=i;
		}
	}
	fout<<char(answer+'a');
	fout<<" ";
	fout<<min_path;
	

}
void calculate(){
	for(int i=0;i<num_node;i++){
		for(int j=0;j<num_node;j++){
			if(i==j)
				continue;
			if(dist[i][j]==0)
				dist[i][j]=9999;
			else
				dist[i][j]+=degree[j];
		}
	}
	for(int i=0;i<num_node;i++){
		for(int j=0;j<num_node;j++){
			for(int k=0;k<num_node;k++){
				if(dist[j][k]>dist[j][i]+dist[i][k])
					dist[j][k]=dist[j][i]+dist[i][k];
			}
		}
	}
}