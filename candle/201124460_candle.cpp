#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("candle.inp");
ofstream fout("candle.out");
//'a'=97
int main()
{
    int floyd_wei[26][26];
    int x_way[26];
    int edge_num;
    char edg[3];
    fin>>edge_num;
    fin>>edg[0]>>edg[1]>>edg[2];
    for(int i=0; i<edge_num; i++){
        for(int j=0; j<edge_num; j++){
            floyd_wei[i][j]=9999;
        }
    }
    for(int i=0; i<edge_num; i++){
        char v1,v2;
        int wei;
        fin>>v1;
        fin>>x_way[v1-97];
        for(int j=0; j<x_way[v1-97]; j++){
            fin>>v2;
            fin>>floyd_wei[v1-97][v2-97];
        }
    }

    for(int k=0; k<edge_num; k++){
        for(int i=0; i<edge_num; i++){
            for(int j=0; j<edge_num; j++){
                if(floyd_wei[i][j] > floyd_wei[i][k]+floyd_wei[k][j]+x_way[k]){
                    floyd_wei[i][j] = floyd_wei[i][k]+floyd_wei[k][j]+x_way[k];
                }
            }
        }
    }
    int result=9999;
    char result_edg;
    for(int j=0; j<edge_num; j++){
        int temp=0;
        for(int i=0; i<3; i++){
            if(floyd_wei[edg[i]-97][j] > temp){
                temp = floyd_wei[edg[i]-97][j];
            }
        }
        if(temp<result){
            result=temp;
            result_edg=97+j;
        }
    }


    fout << result_edg << " ";
    fout << result;

    return 0;
}
