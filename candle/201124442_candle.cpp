#include <iostream>
#include <fstream>
#define MAX 999999
using namespace std;
int dist[26][26];
int n;
char vertex[3];
int degree[26];
void floyd(){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(i == j) continue;
            if (dist[i][j] == 0) dist[i][j] = MAX;
            else dist[i][j] += degree[j];
        }
    }
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}
int main(){
    ifstream inStream("candle.inp");
    ofstream outStream("candle.out");
    inStream >> n;
    for(int i = 0; i < 3; i++) inStream >> vertex[i];
    for(int i = 0; i < n; i++){
        char tempChar;
        int tempDegree;
        inStream >> tempChar;
        inStream >> tempDegree;
        degree[tempChar - 'a'] = tempDegree;
        for(int j = 0; j < tempDegree; j++){
            char tempChar_2;
            inStream >> tempChar_2;
            inStream >> dist[tempChar-'a'][tempChar_2 - 'a'];
        }
    }
    floyd();
    int index = 0;
    int minPath = MAX;
    for(int i = 0; i < n; i++){
        int temp = 0;
        for(int j = 0; j < 3; j++){
            if(temp < dist[vertex[j]-'a'][i] - degree[i])
                temp = dist[vertex[j]-'a'][i] - degree[i];
        }
        if(minPath > temp){
            minPath = temp;
            index = i;
        }
    }
    outStream << (char)(index + 'a') << " " << minPath << endl;
    return 0;
}
