#include <bits/stdc++.h>
using namespace std;
int n;
char a,b,c,ans,cur,d;
int curn,e,minx=1e9;
int v[27][27];
int deg[27];
int main(){
	freopen("candle.inp","r",stdin);
	freopen("candle.out","w",stdout);
	cin>>n;
	cin>>a>>b>>c;
	a-='a';
	b-='a';
	c-='a';
	memset(v,10,sizeof(v));
	for(int i=0;i<n;++i){
		cin>>cur;
		cur-='a';
		cin>>deg[cur];
		for(int i=0;i<deg[cur];++i){
			cin>>d>>e;
			v[cur][d-'a']=deg[cur]+e;
		}
	}
	for(int k=0;k<n;++k){
		for(int i=0;i<n;++i){
			for(int j=0;j<n;++j){
				v[i][j]=min(v[i][j],v[i][k]+v[k][j]);
			}
		}
	}
	for(int i=0;i<n;++i){
		int t = max({v[a][i]-deg[a],v[b][i]-deg[b],v[c][i]-deg[c]});
		if(t<minx){
			minx=t;
			ans=i;
		}
	}
	cout<<char(ans+'a')<<' '<<minx;
}