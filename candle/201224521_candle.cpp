#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;


int main(){
	ifstream inFile("candle.inp");
	ofstream outFile("candle.out");
	int count, change;
	int map[26][26], map2[26][26], deg[26];
	int i, j, k, p, tmp, tmp2, min; //calc max ( i->j , i->k->j 
	char s1, s2, s3;
	int i1, i2, i3;
	char start_node, end_node;
	int node_count, row, col;
	
	inFile>>count>>s1>>s2>>s3;
	
	i1 = s1-'a';
	i2 = s2-'a';
	i3 = s3-'a';
	
	//initial
	for(i=0;i<count; i++){
		for(j=0;j<count;j++){
			if(i==j) map[i][j]=0;
			else map[i][j]=0x7fffff;
		}
	}
	
	//input
	for(i=0;i<count; i++){
		inFile>>start_node>>node_count;
		row=start_node-'a';
		deg[row]=node_count;
		//cout<<node_count<<endl;
		for(j=0;j<node_count;j++){
			inFile>>end_node>>tmp;
			col=end_node-'a';
			map[row][col]=tmp; //row -> col
			//cout << tmp << endl;
		}
	}
	
	//for(i=0; i<count i++)	for(j=0; j<count; j++) map2[row][col]=map[row][col]

	
	//shortest long path
	for(p=0;p<count; p++){ //n try...
		change=0;
		for(i=0;i<count;i++){
			for(j=0;j<count;j++){
				tmp = map[i][j];
				for(k=0;k<count;k++){
					tmp2 = map[i][k]+map[k][j]+deg[k]; //new one + original one
					if(tmp>tmp2){
						//cout <<(char)(i+'a')<<" "<<(char)(k+'a')<<" "<<(char)(j+'a')<<" "<< map[i][k]<<" "<<map[k][j]<< " "<<deg[k]<<"     " <<tmp<<" "<<tmp2<<endl;
						change++;
						map[i][j]=tmp2;
						tmp = tmp2;
					}
				}
			}
		}
		if(change==0){
			break;
		} 
	}
	
	//cout<<map[i1]['d'-'a']+map[i2]['d'-'a']+map[i3]['d'-'a']<<endl;
	//cout <<'d'-'a';
	
	min = 0x7fffff;
	for(i=0;i<count;i++){
		tmp=map[i1][i];
		tmp2 = map[i2][i];
		if(tmp2>tmp) tmp=tmp2;
		tmp2=map[i3][i];
		if(tmp2>tmp) tmp=tmp2;
		if(tmp<min){
			end_node=i+'a';
			min=tmp;
		}
	}
	outFile<< end_node << " " << min;
}


