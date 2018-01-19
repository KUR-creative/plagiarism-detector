#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>

using namespace std;

int edges[26][26];
int EdgeDist[26][26];
int NumOfEdge[26];

int minDist(bool sptset[], int src) {
    int minVal = 999999;
    int MinIndex;

    for(int i = 0; i < 26; i++) {
        if(sptset[i] == false && EdgeDist[src][i] <= minVal) {
            minVal = EdgeDist[src][i];
            MinIndex = i;
        }
    }

    return MinIndex;
}

void findMinPath(int src) {
    int previous[26];
    bool sptset[26];

    int parent[26];

    for(int i = 0; i < 26; i++) {
        parent[i] = -1;
        sptset[i] = false;
    }

    for(int Count = 0; Count < 25; Count++) {
        int u = minDist(sptset, src);

        sptset[u] = true;

        for(int v = 0; v < 26; v++) {
            if(!sptset[v] && edges[u][v] != 0) {
                if(parent[u] != -1) {
                    if(EdgeDist[src][u] + edges[u][v] + NumOfEdge[u] < EdgeDist[src][v]) {
                        EdgeDist[src][v] = EdgeDist[src][u] + edges[u][v] + NumOfEdge[u];
                        parent[v] = u;
                    }
                } else {
                    if(EdgeDist[src][u] + edges[u][v] < EdgeDist[src][v]) {
                        EdgeDist[src][v] = EdgeDist[src][u] + edges[u][v];
                        parent[v] = u;
                    }
                }
            }
        }
    }
}

int findMaxVal(int a, int b, int c) {
    int MaxVal = a;

    if(MaxVal < b)
        MaxVal = b;
    if(MaxVal < c)
        MaxVal = c;

    return MaxVal;
}


int main() {
    ifstream candleIN("candle.inp");
    ofstream candleOUT("candle.out");

    int NumVertex;
    char Svertex;
    char Dvertex;
    int edgeNum;
    int dist;
    char peoples[3];
    int IntPeople[3];

    for(int i = 0; i < 26; i++) {
        for(int j = 0; j < 26; j++) {
            if(i == j) {
                EdgeDist[i][j] = 0;
            } else {
                EdgeDist[i][j] = 999999;
            }
            edges[i][j] = 0;
        }
        NumOfEdge[i] = 0;
    }

    candleIN >> NumVertex;
    candleIN >> peoples[0] >> peoples[1] >> peoples[2];

    IntPeople[0] = (int)peoples[0] - 97;
    IntPeople[1] = (int)peoples[1] - 97;
    IntPeople[2] = (int)peoples[2] - 97;

    for(int i = 0; i < NumVertex; i++) {
        candleIN >> Svertex >> edgeNum;
        for(int j = 0; j < edgeNum; j++) {
            candleIN >> Dvertex >> dist;
            edges[(int)Svertex - 97][(int)Dvertex - 97] = dist;
            NumOfEdge[(int)Svertex - 97]++;
        }
    }

    for(int i = 0; i < 26; i++) {
        findMinPath(i);
    }

    int minMaxPath = 999999;
    int minMaxPoint;
    char CharPoint;
    int newValue;

    for(int i = 0; i < 26; i++) {
        newValue = findMaxVal(EdgeDist[i][IntPeople[0]], EdgeDist[i][IntPeople[1]], EdgeDist[i][IntPeople[2]]);
        if(minMaxPath > newValue) {
            minMaxPath = newValue;
            minMaxPoint = i + 97;
        }
    }
    CharPoint = (char)minMaxPoint;
    candleOUT << CharPoint << " " << minMaxPath;
    return 0;
}
