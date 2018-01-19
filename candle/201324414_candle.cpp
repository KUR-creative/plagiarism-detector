#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <climits>
using namespace std;

#define MAX_N 26
int N;
int fr[3];


vector<pair <int, int> > adj [MAX_N];

int global_dest = -1;
int global_min = INT_MAX;

vector<int> dijkstra_cache[3];
//backtracking
void find_min_time(int dest){
    int path_1 = dijkstra_cache[0][dest];
    if (path_1 >= global_min)
        return;

    int path_2 = dijkstra_cache[1][dest];
    if (path_2 >= global_min)
        return;

    int path_3 = dijkstra_cache[2][dest];
    if (path_3 >= global_min)
        return;

    int min_value = max(path_1, path_2);
    min_value = max(min_value, path_3);
    global_min = min_value;
    global_dest = dest;
}

vector<int> dijkstra(int src){
    vector<int> dist(N, INT_MAX);
  //  vector<int> dist_degree(N, INT_MAX);
    priority_queue<pair <int,int> > pq;
    dist[src] = 0;

    pq.push(make_pair(0,src));
    while (!pq.empty()){
        int cost = pq.top().first;
        int here = pq.top().second;
        int degree = adj[here].size();

        if (here == src) degree = 0;

        pq.pop();

        if (dist[here] < cost){
            continue;
        }
        for (int i = 0 ; i < adj[here].size() ; i++){
            int there = adj[here][i].first;
            int next_cost = degree + cost + adj[here][i].second;
            if (next_cost < dist[there]){
                pq.push(make_pair(next_cost, there));
                dist[there] = next_cost;
            }
        }
    }
    return dist;
}

int main(){

    FILE *fin = fopen("candle.inp", "r");

    fscanf(fin, "%d" , &N);
    char friend_alph[3];
    fscanf(fin, " %c %c %c", &friend_alph[0], &friend_alph[1], &friend_alph[2]);

    for (int i = 0 ; i < 3 ; i++)
        fr[i] = friend_alph[i] - 'a';

    for (int i = 0 ; i < N ; i++){
        char src;
        int edge_num;

        fscanf(fin," %c %d",&src,&edge_num);
        for (int j = 0 ; j < edge_num ; j++){
            char dest;
            int weight;
            fscanf(fin," %c %d",&dest,&weight);
            adj[src-'a'].push_back(make_pair(dest-'a',weight));

        }
    }

    for (int i = 0 ; i < 3 ; i++){
        dijkstra_cache[i] = dijkstra(fr[i]);
    }

    for (int i = 0 ; i < N ; i++){
        find_min_time(i);
    }

    ofstream(fout);
    fout.open("candle.out");

    cout << (char)(global_dest+'a') <<" " << global_min << endl;
    fout << (char)(global_dest+'a') <<" " << global_min << endl;

    return 0;
}
