#include <vector>
#include <iostream>
#include <fstream>
#include <list>
#include <set>
#include <string>
#include <iterator>
#define ctoi(xxx) xxx - 'a'
#define INTMAX 2147483647
using namespace std;

ifstream				fin("candle.inp");
ofstream				fout("candle.out");
vector<vector<int> >	edge_weight(26, vector<int>(26));
vector<int>				vertex_weight(26);
vector<list<int> >		connected_edge(26);
char					start_p[3];
int						num_vertex;

void read_file() {
	int		num_edge, weight_edge;
	char	this_vertex, connected_vertex;
	fin >> num_vertex >> start_p[0] >> start_p[1] >> start_p[2];
	
	for (int i = 0; i < num_vertex; i++) {
		fin >> this_vertex >> num_edge;
		vertex_weight[ctoi(this_vertex)] = num_edge;
		while (num_edge--) {
			fin >> connected_vertex;
			fin >> edge_weight[ctoi(this_vertex)][ctoi(connected_vertex)];
			connected_edge[ctoi(this_vertex)].push_back(ctoi(connected_vertex));
		}
	}
}

int min_vertex(vector<int> _temp) {
	int min_vertex, min_distance = INTMAX;
	for (int i = 0; i < _temp.size(); i++) {
		if (min_distance > _temp[i]) {
			min_vertex = i;
			min_distance = _temp[i];
		}
	}
	return min_vertex;
}

vector<int> trasformed_dijkstra_algorithm(int start_p) {
	vector<int> distance(num_vertex, INTMAX), temp;
	set<int>	decided_vertex, undecided_vertex;
	int			last_decided_vertex = start_p, removed_vertex_weight;

	decided_vertex.insert(start_p);
	for (int i = 0; i < num_vertex; i++) {
		if (i == start_p) {
			distance[i] = 0;
			continue;
		}
		undecided_vertex.insert(i);
	}
	
	removed_vertex_weight = vertex_weight[start_p];
	vertex_weight[start_p] = 0; //시작점에서는 vertex가 필요없으므로.

	while (!undecided_vertex.empty()) {
		for (auto it = connected_edge[last_decided_vertex].begin(); 
			it != connected_edge[last_decided_vertex].end(); it++) {
			int sum_distance = vertex_weight[last_decided_vertex] + 
				edge_weight[last_decided_vertex][*it] + distance[last_decided_vertex];

			distance[*it] = distance[*it] > sum_distance ? sum_distance : distance[*it];
		}
		temp = distance;

		for (auto it = decided_vertex.begin(); it != decided_vertex.end(); it++)
			temp[*it] = INTMAX;

		last_decided_vertex = min_vertex(temp);
		decided_vertex.insert(last_decided_vertex);
		undecided_vertex.erase(last_decided_vertex);
	}
	vertex_weight[start_p] = removed_vertex_weight;
	return distance;
}

int max(int a, int b, int c) {
	int x = a > b ? a : b;
	x = x > c ? x : c;
	return x;
}

void compute_result(){
	vector<vector<int> >	result_from_3p(3);
	vector<int>				final_result(num_vertex);
	int						min_distance = INTMAX, min_vertex;

	for (int i = 0; i < 3; i++) {
		result_from_3p[i] = trasformed_dijkstra_algorithm(ctoi(start_p[i]));
	}
	for (int i = 0; i < num_vertex; i++) {
		final_result[i] = max(result_from_3p[0][i], result_from_3p[1][i], result_from_3p[2][i]);
	} // max
	for (int i = 0; i < final_result.size(); i++) {
		if (min_distance > final_result[i]) {
			min_distance = final_result[i];
			min_vertex = i;
		}
	} // maxmin
	fout << (char)(min_vertex + 'a') << " " << min_distance;
}

int main() {
	read_file();
	compute_result();
}
