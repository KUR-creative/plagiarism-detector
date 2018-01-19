#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <stack>
#define INF 999999
#define IS_PRINT -1
using namespace std;
int numOfNode = 0;
int vtxMap[99999];
int** nhbWeight;
int** shortestPath;
int** shortestPath2;
int** route;
stack<int>* routeWeight;
char A,B,C;
FILE* candleInput = fopen("candle.inp","r");
FILE* candleOutput = fopen("candle.out","w");
class Node{
public:
	char name;
	int numOfEdge;
	Node* neighbors;
	int registNeighborCount;
	int weight;
	int* distance;
	int idx;
	Node(){
		name = '#';
		numOfEdge = 0;
		weight = 0;
		registNeighborCount = -1;
		idx = 0;
	}

	Node(char _name,int _numOfEdge, int _idx){
		name = _name;
		weight = 0;
		numOfEdge = _numOfEdge;
		registNeighborCount = -1;
		idx = _idx;
	}

	int initNeighbor(){

		if(numOfEdge == 0)return -1;

		neighbors = new Node[numOfEdge];
		registNeighborCount = 0;

		return 0;

	}

	int addNeighbor(char _name,int _weight){
		if(registNeighborCount == numOfEdge)return -1;
		
		neighbors[registNeighborCount].name = _name;
		neighbors[registNeighborCount].weight = _weight;
		registNeighborCount++;
		return 0;
	}

	int initDistance(){
		distance = new int[numOfNode];
		for(int i = 0 ; i < numOfNode ; i++)distance[i] = INF;
		distance[vtxMap[(int)name]] = 0;

		for(int i = 0 ; i < numOfEdge ; i++){
			distance[vtxMap[(int)neighbors[i].name]] = neighbors[i].weight;
			
		}
		
	}
};

Node* vtxs;

void readData();

int startNodes[3];


int getPathWeight(int v1, int v2){

	if(v1 == v2)return 0;

	int totalWeight = 0;
	routeWeight[v1].push(v2);
	
	
	routeWeight[v1].push(route[v1][v2]);
	
	
	while(route[v1][routeWeight[v1].top()] != 999999){
			
		routeWeight[v1].push(route[v1][routeWeight[v1].top()]);
		
	}
	
	
	//routeWeight[v1].pop();
	int node_temp = v1;

	int cnt = 0;
	while(!routeWeight[v1].empty()){
		cnt++;	


		int currrent = routeWeight[v1].top();

		//if(node_temp != currrent){
			totalWeight += nhbWeight[node_temp][currrent];
			//totalWeight += nhbWeight[currrent][node_temp];
			totalWeight += vtxs[currrent].numOfEdge;
		//}
		//cout << vtxs[currrent].numOfEdge << ' ';

		if(IS_PRINT == 1)cout <<  vtxs[routeWeight[v1].top()].name  << ' ' ;
		routeWeight[v1].pop();

		node_temp = currrent;

	}
	if(IS_PRINT == 1)cout << endl;
	totalWeight -= vtxs[v1].numOfEdge;
	if(cnt != 0)totalWeight -= vtxs[node_temp].numOfEdge;

	if(IS_PRINT == 1)printf("Node %c <---> %c  , Weight : %5d\n",vtxs[v1].name,vtxs[v2].name,totalWeight);

	return totalWeight;

}

int returnMaximum(int r1,int r2,int r3){
	if(r1 > r2){
		if(r1 > r3){
			return r1;
		}else{
			return r3;
		}
	}else{
		if(r2 > r3){
			return r2;
		}else{
			return r3;
		}
	}
}

void findShortestPath(){

	for(int i = 0 ; i < numOfNode ; i++){
	
		for(int j = 0 ; j < numOfNode ; j++){
		// start node
			for(int k = 0 ; k < numOfNode ; k++){
				
				if( shortestPath[k][j] > shortestPath[k][i] + shortestPath[i][j] + vtxs[i].numOfEdge){
					shortestPath[k][j] = shortestPath[k][i] + shortestPath[i][j] + vtxs[i].numOfEdge;
					
					route[k][j] = route[i][j];
					
				}
			}

			//cout << endl;

		}
	}
	if(IS_PRINT == 1){
		printf("------");
		for(int i = 0 ; i < numOfNode ; i++)printf("%7c ",vtxs[i].name);
		cout << endl;
		for(int i = 0 ; i < numOfNode ; i++){
			printf("%7c ",vtxs[i].name);
			for(int j = 0 ; j < numOfNode ; j++){
				printf("%7d ",route[i][j]);
			}
			cout << endl;
		}

		printf("------");
		for(int i = 0 ; i < numOfNode ; i++)printf("%5c ",vtxs[i].name);
		cout << endl;
		for(int i = 0 ; i < numOfNode ; i++){
			printf("%5c ",vtxs[i].name);
			for(int j = 0 ; j < numOfNode ; j++){
				printf("%5d ",shortestPath[i][j]);
			}
			cout << endl;
		}
	}

	char candlePoint = '*';
	int min = 9999999;

	for(int i = 0 ; i < numOfNode ; i++){
		int temp = returnMaximum(
			getPathWeight(vtxMap[(int)A],i),
			getPathWeight(vtxMap[(int)B],i),
			getPathWeight(vtxMap[(int)C],i));

		if(temp <= min){
			min = temp;
			candlePoint = vtxs[i].name;
		}
	}
	
	//cout << candlePoint << ' ' << min << endl;
	fprintf(candleOutput,"%c %d\n",candlePoint,min);
	

}

int main(){

	readData();
	findShortestPath();
	fclose(candleInput);
	fclose(candleOutput);

	return 0;

}



void readData(){

	fscanf(candleInput,"%d", &numOfNode);
	
	
	vtxs = new Node[numOfNode];	
	nhbWeight = new int*[numOfNode];
	shortestPath = new int*[numOfNode];
	shortestPath2 = new int*[numOfNode];
	route = new int*[numOfNode];
	routeWeight = new stack<int>[numOfNode];

	for(int i = 0 ; i < numOfNode ; i++){
		shortestPath[i] = new int[numOfNode];
		shortestPath2[i] = new int[numOfNode];
		route[i] = new int[numOfNode];
		nhbWeight[i] = new int[numOfNode];

		for(int j = 0 ; j < numOfNode; j++){
			
			shortestPath[i][j] = INF;
			shortestPath2[i][j] = INF;
			nhbWeight[i][j] = 0;

			route[i][j] = INF;
			
			if(i == j)shortestPath[i][j] = 0;
			if(i == j)nhbWeight[i][j] = 0;
		
		}
	}

	fscanf(candleInput,"%s %s %s",&A,&B,&C);
	

	for(int i = 0 ; i < numOfNode ; i++){

		vtxs[i].idx = i;
		

		fscanf(candleInput,"%s %d",&vtxs[i].name,&vtxs[i].numOfEdge);
		
		vtxMap[(int)vtxs[i].name] = i;
		vtxs[i].initNeighbor();
		
		for(int j = 0 ; j < vtxs[i].numOfEdge ; j++){
			char name;
			int weight;
			fscanf(candleInput,"%s %d",&name,&weight);
			vtxs[i].addNeighbor(name,weight);

		}
		
	}


	for(int i = 0 ; i < numOfNode ; i++){

		vtxs[i].initDistance();

	}



	for(int i = 0 ; i < numOfNode; i++){

		for(int j = 0 ; j < vtxs[i].numOfEdge ; j++){
			
			nhbWeight[i][vtxMap[(int)vtxs[i].neighbors[j].name]]    =	vtxs[i].neighbors[j].weight;
			shortestPath[i][vtxMap[(int)vtxs[i].neighbors[j].name]] = vtxs[i].neighbors[j].weight;
			shortestPath[vtxMap[(int)vtxs[i].neighbors[j].name]][i] = vtxs[i].neighbors[j].weight;
			shortestPath2[i][vtxMap[(int)vtxs[i].neighbors[j].name]] = vtxs[i].neighbors[j].weight;
			shortestPath2[vtxMap[(int)vtxs[i].neighbors[j].name]][i] = vtxs[i].neighbors[j].weight;


			//route[i][vtxMap[(int)vtxs[i].neighbors[j].name]] = vtxMap[(int)vtxs[i].neighbors[j].name];
			route[i][vtxMap[(int)vtxs[i].neighbors[j].name]] = i;
			//cout << vtxMap[(int)vtxs[i].neighbors[j].name] << " " ;
			//route[vtxMap[(int)vtxs[i].neighbors[j].name]][i] = vtxMap[(int)vtxs[i].neighbors[j].name];
		}
		//cout << endl;
		
	}
	
	if(IS_PRINT == 1){
		printf("------");
		for(int i = 0 ; i < numOfNode ; i++)printf("%7c ",vtxs[i].name);
		cout << endl;
		for(int i = 0 ; i < numOfNode ; i++){
			printf("%7c ",vtxs[i].name);
			for(int j = 0 ; j < numOfNode ; j++){
				printf("%7d ",nhbWeight[i][j]);
			}
			cout << endl;
		}
	}
	


}