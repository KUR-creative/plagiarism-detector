#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef double pt[3];


void set_pt(istream& is, pt& p)
{
	for(int i=0;i<3;++i)
		is >> p[i];
}

double dist(pt& p1, pt& p2) 
{
	double d=0;
	for(int i=0;i<3;++i)
		d+=pow(p1[i]-p2[i],2);
	return sqrt(d);
}

void center_pt(pt& p1, pt& p2, pt& p3) 
{
	for(int i=0;i<3;++i)
		p3[i]=(0.5)*(p1[i]+p2[i]);
}

double reset_d2(pt& p1, pt& p2, pt& p3, pt& p) 
{
	center_pt(p1,p2,p3);
	return dist(p3,p);
}

int main(void)
{
	pt a,b,c,p;

	ifstream ifs("connect.inp");
	set_pt(ifs,a);
	set_pt(ifs,b);
	set_pt(ifs,p);
	ifs.close();
	
	center_pt(a,b,c);
	
	vector<double> d;
	d.push_back(dist(a,p));
	d.push_back(dist(b,p));
	d.push_back(dist(c,p));
	
	sort(d.begin(), d.end());
	while( (d[2]-d[0])>0.5 ) {
		if(dist(a,p)==d[2]) {
			d[2]=reset_d2(b,c,a,p);
		}
		else if(dist(b,p)==d[2]) {
			d[2]=reset_d2(a,c,b,p);
		}
		else {
			d[2]=reset_d2(a,b,c,p);
		}
		sort(d.begin(), d.end());
	}
	
	ofstream ofs("connect.out");
	ofs << ceil(d[0]) << endl;
	ofs.close();
	return 0;
}
