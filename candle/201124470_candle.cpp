#include <iostream>
#include <algorithm>
#include <fstream>

#define MAX 27

using namespace std;

int t[MAX][MAX];
int degree[MAX];
int sp[3];

int changeIndex(char c){
    return c - 'a' + 1;
}

int main(){
    ifstream fin("candle.inp");
    ofstream fout("candle.out");
    int n;
    fin >> n;

    for(int i = 0 ; i < 3 ; ++i){
        char c; fin >> c;
        sp[i] = changeIndex(c);
    }

    for(int i = 1; i <= n ; ++i)
        fill(t[i], t[i] + n + 1 , 2e9);

    for(int i = 1 ; i <= n ; ++i ){
        char c; int e ; fin >> c >> e;
        int str = changeIndex(c);
        degree[str] = e;
        for(int j = 1 ; j <= e ; ++j){
            int v; fin >> c >> v;
            int dst = changeIndex(c);
            t[dst][str] = t[str][dst] = v;
        }
    }

    for(int i = 1; i <= n ; ++i){
        for(int j = 1 ; j <= n ; ++j){
            if(t[j][i] == 2e9) continue;
            for(int k = 1 ; k <= n ; ++k){
                if(j != k  && t[i][k] != 2e9){
                    int tmp = t[j][i] + t[i][k] + degree[i];
                    if(t[j][k] > tmp)
                        t[j][k] = tmp;
                }
            }
        }
    }

    for(int i = 1; i <= n ; ++i)
        t[i][i] = 0;

    char ac;
    int aval = 2e9;

    for(int i = 1; i <= n ; ++i){
        int tval = max(t[sp[0]][i], max(t[sp[1]][i], t[sp[2]][i]));
        if(tval < aval){
            aval = tval;
            ac = i + 'a' - 1;
        }
    }

    fout << ac << " " << aval << endl;
}
