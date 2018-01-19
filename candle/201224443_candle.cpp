#include <iostream>
#include <fstream>
#include <cstdio>

#define max(a,b) ((a) > (b) ? (a) : (b))

using namespace std;

FILE* inFile = fopen("candle.inp", "r") ;
FILE* outFile = fopen("candle.out", "w") ;

int routeGraph[26][26] ;
int friends[3] ;
int visit[3][26] ;
int dist[3][26] ;
int vertexOfDegree[26] ;
int maxDist[26] ;
int numOfNode ;
int minDistOfMaxDist = 99999 ;
char meetVertex ;

void dijkstra(int startNode, int friendsNum) ;

int main() {
    fscanf(inFile, "%d %s %s %s", &numOfNode, &friends[0], &friends[1], &friends[2]) ;
    friends[0] -= 97 ;
    friends[1] -= 97 ;
    friends[2] -= 97 ;

    for ( int i = 0 ; i< numOfNode ; i ++) {
        for (int j = 0 ; j< numOfNode ; j ++) {
            routeGraph[i][j] = 99999 ;
        }
    }

    for (int i = 0 ; i < numOfNode ; i ++) {
        dist[0][i] = 99999 ;
        dist[1][i] = 99999 ;
        dist[2][i] = 99999 ;
        int vertexNum = 0 ;
        int numOfDegree = 0 ;
        fscanf(inFile, "%s %d", &vertexNum, &numOfDegree) ;
        vertexNum -= 97 ;
        vertexOfDegree[vertexNum] = numOfDegree ;

        for (int j = 0 ; j < numOfDegree ; j ++) {
            int nextVertexNum = 0 ;
            int betweenWeight = 0 ;
            fscanf(inFile, "%s %d", &nextVertexNum, &betweenWeight) ;
            nextVertexNum -= 97 ;
            routeGraph[vertexNum][nextVertexNum] = betweenWeight ;
        }
    }

    /*
    cout << endl ;
    for (int i = 0 ; i < numOfNode ; i ++) {
        for (int j = 0 ; j < numOfNode ; j ++)  {
            cout << routeGraph[i][j] << "\t" ;
        }
        cout << endl ;
    }
    cout << endl ;
    */
    dijkstra(friends[0], 0) ;
    dijkstra(friends[1], 1) ;
    dijkstra(friends[2], 2) ;
    /*
    for (int i = 0 ; i < 3 ; i ++) {
        for (int j = 0 ; j < numOfNode ; j ++) {
            cout << dist[i][j] << "\t" ;
        }
        cout << endl ;
    }
    */
    for (int j = 0 ; j < numOfNode ; j ++) {
        int distTemp = max(dist[0][j], max(dist[1][j], dist[2][j])) ;
        if (minDistOfMaxDist > distTemp) {
            minDistOfMaxDist = distTemp ;
            meetVertex = (char)(j+97) ;
        }
    }
    //cout << meetVertex << " " << minDistOfMaxDist << endl ;
    fprintf(outFile, "%c %d\n", meetVertex, minDistOfMaxDist) ;

    return 0 ;
}

void dijkstra(int startNode, int friendsNum) {
    int temp = vertexOfDegree[startNode] ;
    vertexOfDegree[startNode] = 0 ;
    dist[friendsNum][startNode] = 0 ;
    int minDist ;
    int vertex ;

    for ( int i = 0 ; i < numOfNode ; i ++) {
        minDist = 99999 ;
        for (int j = 0 ; j < numOfNode ; j ++) {
            if ( visit[friendsNum][j] == 0 && minDist > dist[friendsNum][j]) {
                minDist = dist[friendsNum][j] ;
                vertex = j ;
            }
        }
        visit[friendsNum][vertex] = 1 ;
        for (int k = 0 ; k < numOfNode ; k ++ ) {
            if ( i == 0 && dist[friendsNum][k] > dist[friendsNum][vertex] + routeGraph[vertex][k] ) {
                dist[friendsNum][k] = dist[friendsNum][vertex] + routeGraph[vertex][k] + vertexOfDegree[vertex] ;
            }
            else if (i != 0 && dist[friendsNum][k] > dist[friendsNum][vertex] + routeGraph[vertex][k] + vertexOfDegree[vertex] ) {
                dist[friendsNum][k] = dist[friendsNum][vertex] + routeGraph[vertex][k] + vertexOfDegree[vertex] ;
            }
        }
    }
    vertexOfDegree[startNode] = temp ;
}

