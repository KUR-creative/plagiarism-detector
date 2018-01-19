#include <iostream>
#include <fstream>
using namespace std;
int candelMap[26][26];
int main()
{
    ifstream finp("candle.inp");
    ofstream fout("candle.out");

    int N;
    finp >> N;

    char f1,f2,f3;
    int fo1,fo2,fo3;

    finp >> f1 >> f2 >> f3;

    for(int i=0;i<26;i++)
        for(int j=0;j<26;j++)
        candelMap[i][j]=999999999;


    int tempi;
    char tempc1, tempc2;
    for(int i=0; i<N; i++){
        finp >> tempc1 >> tempi;
        if( tempc1 == f1) fo1=tempi;
        if( tempc1 == f2) fo2=tempi;
        if( tempc1 == f3) fo3=tempi;
        //cout << tempc1 << " " << tempi <<endl;
        for(int j=0; j<tempi; j++){
            finp >> tempc2;
            finp >> candelMap[tempc1-'a'][tempc2-'a'];
            candelMap[tempc1-'a'][tempc2-'a'] +=tempi;
            //cout << candelMap[tempc1-'a'][tempc2-'a'] << endl;;
        }
    }

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<N; k++){
                candelMap[j][k]=
                min(candelMap[j][k], candelMap[j][i]+candelMap[i][k]);
            }
        }
    }
    
	for(int i=0; i<N; i++){
    	for(int j=0; j<N; j++){
    		cout << candelMap[i][j] << " ";
		}
		cout << endl;
	}
	int cost=9999999;
	char rst='a';
    for(int i=0; i<N; i++){
    	if(cost > max(candelMap[f1-'a'][i]-fo1,max(candelMap[f2-'a'][i] -fo2,candelMap[f3-'a'][i] -fo3 )) ){
    		cost = max(candelMap[f1-'a'][i]-fo1,max(candelMap[f2-'a'][i] -fo2,candelMap[f3-'a'][i] -fo3 ));
			rst = i+'a';	
		}
    }
    
    fout << rst << " "<<cost;
    return 0;
}
