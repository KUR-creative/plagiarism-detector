#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 26;
const int INF = 2e9;

int N;
int friends[3];
vector<pair<int, int>> adj[MAX_N];

vector<int> shortestPath(int src) {
    vector<int> dist(N, INF);
    dist[src] = 0;
    priority_queue<pair<int, int>> pq;
    pq.push({0, src});
    while (!pq.empty()) {
        int cost = -pq.top().first;
        int here = pq.top().second;
        pq.pop();
        if (dist[here] < cost) continue;
        int degreeOfHere = adj[here].size();
        for (int i = 0; i < degreeOfHere; i++) {
            int there = adj[here][i].first;
            int tempCost = adj[here][i].second + cost;
            if (here != src) tempCost += degreeOfHere;
            if (dist[there] <= tempCost) continue;
            dist[there] = tempCost;
            pq.push({-tempCost, there});
        }
    }
    return dist;
}

void solve() {
    vector<int> dist1 = shortestPath(friends[0]);
    vector<int> dist2 = shortestPath(friends[1]);
    vector<int> dist3 = shortestPath(friends[2]);
    int minDist = INF;
    int minVertex;
    for (int i = 0; i < N; i++) {
        int cand = max(max(dist1[i], dist2[i]), dist3[i]);
        if (minDist > cand) {
            minDist = cand;
            minVertex = i;
        }
    }
    cout << (char)(minVertex + 'a') << ' ' << minDist;
}

int main() {
    freopen("candle.inp", "r", stdin);
    freopen("candle.out", "w", stdout);
    cin >> N;
    for (int i = 0; i < 3; i++) {
        char ch;
        cin >> ch;
        friends[i] = ch - 'a';
    }
    for (int i = 0; i < N; i++) {
        char here;
        int numOfEdges;
        cin >> here >> numOfEdges;
        for (int j = 0; j < numOfEdges; j++) {
            char there;
            int edgeWeight;
            cin >> there >> edgeWeight;
            adj[here - 'a'].push_back({ there - 'a', edgeWeight });
        }
    }
    solve();
}
