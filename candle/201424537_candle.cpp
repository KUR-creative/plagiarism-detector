#include <iostream>
#include <fstream>
#include <vector>
#include <array>
using namespace std;
void doFloyd();
int max3(int a, int b, int c);
int dist(int i, int j, int k);
int candleGraph[26][26];
int candleNode[26];

int MinCost[26][26];
int MaxRoute[26];

int N;

int main()
{
	ifstream fin("candle.inp");
	ofstream fout("candle.out");
	fin >> N;
	int start[3];
	char tmp;
	for (int i = 0; i < 3; i++)
	{
		fin >> tmp;
		start[i] =tmp- 'a';
	}

	for (int i = 0; i < N; i++)
	{
		int idxV;
		fin >> tmp;
		idxV =tmp- 'a';
		int NumV;
		fin >> NumV;
		candleNode[idxV] = NumV;
		for (int j = 0; j < NumV; j++)
		{
			int idxN;
			fin >> tmp;
			idxN = tmp-'a';
			int weightN;
			fin >> weightN;
			candleGraph[idxV][idxN] = weightN;
		}
	}

	doFloyd();
	int Max = 10000000;
	int idx = 0;
	for (int i = 0; i < N; i++)
	{
		MaxRoute[i] = max3(MinCost[start[0]][i], MinCost[start[1]][i], MinCost[start[2]][i]);
		if (MaxRoute[i] < Max)
		{
			idx = i;
			Max = MaxRoute[i];
		}
	}

	fout << (char)(idx + 'a') << " " << Max;

	return 1;
}


void doFloyd()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if(candleGraph[i][j] !=0)
				MinCost[i][j] = candleGraph[i][j];
			else
				MinCost[i][j] = 10000000;
			
		}
	}
	for (int i = 0; i < N; i++)
		MinCost[i][i] = 0;

	for (int k = 0; k < N; ++k)
	{
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			{
				if (i == 0 && j == 3)
					MinCost[i][j]+=0;
				if (MinCost[i][j] >dist(i,j,k))
				{
					MinCost[i][j] = dist(i, j, k);
				}
			}
		}
	}

}

int max3(int a, int b, int c)
{ 
	int max = a > b ? a : b;
	return max > c ? max : c;
}


int dist(int i,int j, int k)
{
	int dis = MinCost[i][k] + MinCost[k][j];
	if (i != k && j != k)
		dis+=candleNode[k];

	return dis;

}