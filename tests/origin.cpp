#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int not_call(void){
    int a = 10;
    int b = 234;
    int c = a + b;
    return c;
}

int main()
{
    double x[3] = {0};
    double y[3] = {0};
    double z[3] = {0};
    double length1, length2;

    ifstream fin;
    fin.open("connect.inp");
    for(int i=0; i<3; i++)
        fin >> x[i] >> y[i] >> z[i];
    fin.close();

    while(1) {
        length1 = sqrt(pow((x[0]-x[2]),2) + pow((y[0]-y[2]),2) + pow((z[0]-z[2]),2));
        length2 = sqrt(pow((x[1]-x[2]),2) + pow((y[1]-y[2]),2) + pow((z[1]-z[2]),2));
        if(length1 > length2) {
            x[0]=(x[0]+x[1])/2;
            y[0]=(y[0]+y[1])/2;
            z[0]=(z[0]+z[1])/2;
        }
        else if(length1 < length2) {
            x[1]=(x[0]+x[1])/2;
            y[1]=(y[0]+y[1])/2;
            z[1]=(z[0]+z[1])/2;
        }
        else
            break;
    }

    ofstream fout;
    fout.open("connect.out");
    fout << ceil(length1);
    fout.close();

    return 0;
}
