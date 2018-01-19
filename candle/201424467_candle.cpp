#include <iostream>
#include <fstream>

using namespace std;

int main () {
  int friends[3], length[26][3];
  int casenum;
  int cgraph[26][26], degree[26];

  char tempc, tempd;
  int tempi, tempj, i, j;

  ifstream fileIn;
  ofstream fileOut;

  fileIn.open("candle.inp");
  fileOut.open("candle.out");

  // get inputs
  fileIn >> casenum;

  for (i = 0; i < 3; i++) {
    fileIn >> tempc;
    friends[i] = tempc - 'a';
  }

  // initiate cgraph
  for (i = 0; i < casenum ; i++) {
    for (j = 0; j < casenum ; j++)
      cgraph[i][j] = 99999;
  }

  // fill in cgraph with inputs
  i = 0;
  while ( !fileIn.eof() ) {
    i++;
    fileIn >> tempc >> tempi;
    degree[tempc-'a'] = tempi;
    for (j = 0; j < tempi; j++) {
      fileIn >> tempd >> tempj;
      cgraph[tempc-'a'][tempd-'a'] = tempj;
    }
  }
  /*
  // print for test
  for (i = 0; i < casenum ; i++)
    cout << (char) (i + 'a') << " " << i << "  ";
  cout << endl;
  
  for (i = 0; i < 3; i++) 
    cout << friends[i] << " ";
  cout << endl;
  for (i = 0; i < casenum ; i++) {
    for (j = 0; j < casenum ; j++)
      cout << cgraph[i][j] << " ";
    cout << endl;
  }
  */
  // find shortest length of all
  for (int k = 0; k < casenum; k++) {
    for (int i = 0; i < casenum; i++) {
      for (int j = 0; j < casenum; j++) {
	if (cgraph[i][j] > cgraph[i][k] + cgraph[k][j]  + degree[k]) {
	  cgraph[i][j] = cgraph[i][k] + cgraph[k][j] + degree[k];
	  
	}
      }
    }
  }

  // initiate if meet at friends'
  for (i = 0; i < 3; i++)
    cgraph[friends[i]][friends[i]] = 0;

  /*
  //test
  cout << endl;
  for (i = 0; i < casenum ; i++) {
    for (j = 0; j < casenum ; j++)
      cout << cgraph[i][j] << " ";
    cout << endl;
  }
*/
  //find out length from 3 points to every nodes
  for (i = 0; i < casenum; i++) {
    for (j = 0; j < 3; j++) {
      length[i][j] = cgraph[friends[j]][i];
    }
  }

  // find min
  int min = length[0][0] + length [0][1] + length[0][2], gatherpoint = 0;
  for (i = 0; i < casenum; i++) {
    //find max time
    int tempmax = length[i][0];
    if (tempmax < length [i][1])
      tempmax = length[i][1];
    if (tempmax < length[i][2])
      tempmax = length[i][2];

    // update if max time is smaller than min
    if (tempmax < min) {
      min = tempmax;
      gatherpoint = i;
    }
  }

  //test
  /*
  cout << endl;
  for (i = 0; i < casenum ; i++) {
    for (j = 0; j < 3 ; j++)
      cout << friends[j] << " to " << i << ": "<< length[i][j] << "   ";
    cout << endl;
  }

  // print answer
  cout << endl << (char) (gatherpoint + 'a') << " " << min << endl;;
  */
  fileOut <<  (char) (gatherpoint + 'a') << " " << min << endl;

  fileIn.close();
  fileOut.close();
  
  return 0;
}
