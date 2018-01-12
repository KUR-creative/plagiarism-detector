#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
//power function : pow( num , exponential )
class triple {
	private:
		double x;
		double y;
		double z;
	public:
		triple() {
			x = 0.0;
			y = 0.0;
			z = 0.0;
		}
		triple(int _x, int _y, int _z) {
			x = _x;
			y = _y;
			z = _z;
		}
		double getx()
		{
			return x;	
		}
		double gety()
		{
			return y;
		}
		double getz()
		{
			return z;
		}
		void putxyz(int _x, int _y, int _z) {
			x = _x;
			y = _y;
			z = _z;
		}
		void putxyz(double _x, double _y, double _z) {
			x = _x;
			y = _y;
			z = _z;
		}
		void print()
		{
			cout << "(" << x << ", " << y << ", "<< z << ")" << endl;
		}
		friend triple operator+(triple t1, triple t2);
		friend triple operator*(int a, triple t);
};
triple operator*(double a, triple t)
{
	t.putxyz(t.getx()*a,t.gety()*a,t.getz()*a);
	return t;
}
triple operator+(triple t1, triple t2)
{
	triple retval;
	retval.putxyz(t1.getx()+t2.getx(),t1.gety()+t2.gety(),t1.getz()+t2.getz());
	
	return retval;
}

double dist(triple a, triple b)
{
	return sqrt( pow(a.getx()-b.getx(),2) + pow(a.gety()-b.gety(),2) + pow(a.getz()-b.getz(),2));
}

int main(void)
{
	ifstream inFile("connect.inp");
	ofstream outFile("connect.out");
	if(inFile.is_open()) {
		//algorithm here
		//use binary search!
		int i = 0;
		int array[9];
		double t1 = 0.0;
		double t2 = 1.0;
		triple a, b, p;
		triple s;
		while(i < 9) {
			inFile >> array[i];
			i++;
			if(!(-1000 <= array[i] <= 1000)) return -1;
		}
		a.putxyz(array[0],array[1],array[2]);
		b.putxyz(array[3],array[4],array[5]);
		p.putxyz(array[6],array[7],array[8]);
		
		while(1){
			double d1, d2;
			s = t1 * b + (1.0 - t1) * a;
			d1 = dist(s,p);
			s = t2 * b + (1.0 - t2) * a;
			d2 = dist(s,p);
			//cout << "d1 : " << d1 << " d2 : " << d2 << endl;
			if(d1 == d2) {
				s = (t1+t2)/2 * b + (1.0 - (t1+t2)/2) * a;
				break;
			}
			else if(d1 > d2) { //if t2 wins(right, left goes right)
				t1 += abs(t2-t1)/2;
			}
			else if(d1 < d2) { //if t1 wins(left, right goes left)
				t2 -= abs(t2-t1)/2;
			}
			
			
		}
		//cout << dist(s,p) << endl;
		cout << ceil(dist(s,p)) << endl;
		outFile << ceil(dist(s,p)) << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
