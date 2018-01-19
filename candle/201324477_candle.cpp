#include <iostream>
#include <fstream>

#define INF 10000

using namespace std;

int Num;
int dist[26][26];
int weight[26];

void dijkstra(int start, int edge[26]) {
    int min;
    int v=0;
    int visit[Num];
    for(int i=0; i<Num; i++) {
        visit[i] = 0;
    }

    edge[start] = 0;

    for(int i=0; i<Num; i++) {
        min = INF;

        for(int j=0; j<Num; j++){
            if(visit[j]==0 && min>edge[j]) {
                min = edge[j];
                v = j;
            }
        }
        visit[v] = 1;

        for(int j=0; j<Num; j++) {
            if(edge[j] > edge[v] + dist[v][j] + weight[v]) {
                edge[j] = edge[v] + dist[v][j] ;
                if(v!=start)
                    edge[j] += weight[v];
            }
        }
    }
}

int max(int a, int b, int c) {
    int temp=max(a, b);
    return max(temp, c);
}
int main()
{

    ifstream fin("candle.inp");
    ofstream fout("candle.out");

    int three[3];

    fin >> Num;
    for(int i=0; i<3; i++) {
        char j;
        fin >> j;
        three[i] = (int)j-97;
    }

    for(int i=0; i<Num; i++) {
        for(int j=0; j<Num; j++) {
            if(i!=j)
                dist[i][j] = INF;
            if(i==j)
                dist[i][j] = 0;
        }
    }

    for(int i=0; i<Num; i++) {
        char fNode;
        int fWeight;
        fin >> fNode >> fWeight;
        weight[(int)fNode-97] = fWeight;
        for(int j=0; j<fWeight; j++) {
            char rNode;
            int rWeight;
            fin >> rNode >> rWeight;
            dist[(int)fNode-97][(int)rNode-97]= rWeight;
        }
    }

    int firstdist[Num];
    int seconddist[Num];
    int thirddist[Num];
    for(int i=0; i<Num; i++){
        firstdist[i] = INF;
        seconddist[i] = INF;
        thirddist[i] = INF;
    }
    dijkstra(three[0], firstdist);
    dijkstra(three[1], seconddist);
    dijkstra(three[2], thirddist);

    int least=INF;
    int index;
    for(int i=0; i<Num; i++) {
        int temp=max(firstdist[i], seconddist[i], thirddist[i]);
        if(least>temp) {
            least = temp;
            index = i;
        }
    }

    fout << char(index+97) << " " << least << endl;


    return 0;
}

