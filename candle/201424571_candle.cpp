#include <iostream>
#include <cstdio>

#define BIGNUM 9999
#define ASC 97
#define max(a, b, c) (((((a) > (b)) ? (a) : (b)) > (c)) ? (((a) > (b)) ? (a) : (b)) : (c))
#define min(a, b) (((a) < (b)) ? (a) : (b))

using namespace std;

int main(void)
{
	FILE * fin = fopen("candle.inp", "r");
	FILE * fout = fopen("candle.out", "w");

	int N;
	char loc[3];
	char fromNode, toNode;
	int fromValue, toValue;
	int ** A;
	int i, j;
	fscanf(fin, "%d\n", &N);

	A = new int * [N];

	for (i = 0; i < N; i++)
	{
		A[i] = new int[N]();
	}
	for (i = 0; i < N; i++)
	{
		for (int j = i + 1; j < N; j++)
		{
			A[i][j] = BIGNUM;
			A[j][i] = BIGNUM;
		}
	}

	fscanf(fin, "%c %c %c\n", &loc[0], &loc[1], &loc[2]);

	for (i = 0; i < N; i++)
	{
		fscanf(fin, "%c %d ", &fromNode, &fromValue);
		for (j = 0; j < fromValue; j++)
		{
			fscanf(fin, "%c %d ", &toNode, &toValue);
			A[(int)fromNode - ASC][(int)toNode - ASC] = toValue;
		}
	}

	// 여기까지 배열 초기화

	int ** b = new int *[N];
	for (int i = 0; i < N; i++)
		b[i] = new int[N];

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			b[i][j] = A[i][j];

	for (int v = 0; v < N; v++)
		b[v][v] = 0;

	//
	
	//for (int i = 0; i < N; i++)
	//{
	//	for (int j = 0; j < N; j++)
	//	{
	//		fprintf(fout, "%d ", A[i][j]);
	//	}
	//	fprintf(fout, "\n");
	//}
	//fprintf(fout, "\n");

	//

	int total = 0;
	int count = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			for (int k = 0; k < N; k++)
				if (b[j][k] > b[j][i] + b[i][k])
				{
					//if (j == 10 && k == 0)
					//{
					//	printf("");
					//}
					for (int l = 0; l < N; l++)
						if (A[i][l] != BIGNUM)
							count++;
					count -= 1;
					if (b[j][k] > b[j][i] + b[i][k] + count)
						b[j][k] = b[j][i] + b[i][k] + count;
					//for (int m = 0; m < N; m++)
					//{
					//	cout << A[j][m] << " ";
					//}
					//cout << endl;
					//for (int m = 0; m < N; m++)
					//{
					//	cout << b[j][m] << " ";
					//}
					//cout << endl;
					//getchar();
					count = 0;
				}
	

	int temp = 0;

	//

	//for (int i = 0; i < N; i++)
	//{
	//	for (int j = 0; j < N; j++)
	//	{
	//		fprintf(fout, "%d ", b[i][j]);
	//	}
	//	fprintf(fout, "\n");
	//}
	//fprintf(fout, "\n");

	

	//for (int i = 0; i < 3; i++)
	//{
	//	int mtmt = (int)loc[i] - ASC;
	//	for (int j = 0; j < N; j++)
	//	{
	//		fprintf(fout, "%d ", b[mtmt][j]);
	//	}
	//	fprintf(fout, "\n");
	//}
	//fprintf(fout, "\n");

	//
	int MIN = BIGNUM;
	int totalValue = 0;
	char totalNode = 0;
	char temptemp = 0;
	for (int i = 0; i < N; i++)
	{
		temp = max((int)b[loc[0] - ASC][i], (int)b[loc[1] - ASC][i], (int)b[loc[2] - ASC][i]);

		if (temp < MIN)
		{
			MIN = temp;
			totalNode = (char)i + ASC;
			totalValue = temp;
		}
	}
	fprintf(fout, "%c %d\n", (char)totalNode, totalValue);
	
	return 0;
}
