#include <bits/stdc++.h>


using namespace std;


const int INF = 1 << 20;
int n;

int ver2num(char v){
    return v - 'a';
}

char friends[3];

int graph[256][256];
int weight[256];


int dijk(char from, char to){
    vector<int> dist(256, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > pq;
    pq.push(make_pair(0, from));
    dist[from] = 0;

    while(!pq.empty()){ 
        int u = pq.top().second;
        pq.pop();

        for(char j='a'; j<='z'; j++){
            if(graph[u][j] != 0){
                char v = j;
                char w = graph[u][j];// + weight[u];
                if(u != from){
                    w += weight[u];
                }

                if(dist[v] > dist[u] + w){
                    dist[v] = dist[u] + w;
                    pq.push(make_pair(dist[v], v));
                } 
            }
        }
    }

    return dist[to];
}
int main(){
    freopen("candle.inp", "r", stdin);
    freopen("candle.out", "w", stdout);


    // 7 + 5 + 2 + 4 + 4 
    cin >> n;

    cin >> friends[0] >> friends[1] >> friends[2];

    while(!cin.eof()){
        char to;
        cin >> to;
        int toNum;
        cin >> toNum;

        weight[to] = toNum;

        for(int i=1; i<=toNum; i++){
            char from;
            cin >> from;
            int fromNum;
            cin >> fromNum;

            graph[from][to] = fromNum;
            graph[to][from] = fromNum; 
        }
    }


    int minDist = INF;
    char minPosition = 'a';
    for(char i='a'; i<='z'; i++){
        auto v = vector<int>({dijk(friends[0], i), dijk(friends[1], i), dijk(friends[2], i)});

        int dist = *std::max_element(
                v.begin(), v.end()
                );
        if(minDist > dist){ 
            minDist = dist;
            minPosition = i;
        }
    }

    cout << minPosition << " " << minDist << endl;




    return 0;
}
