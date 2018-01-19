#include <iostream>
#include <fstream>

using namespace std;

ifstream input("candle.inp");
ofstream output("candle.out");
int totalNode;

int* nodeArr;
int* degreeArr;
int distArr[26][26];

void  dijkstra( char c, int dist[26] ){
    bool visit[26] ;
    for( int i=0; i<26; i++){
        visit[i] =false;
    }
    
    dist[ (int)c -97] =0;
    
    
    for( int i=0; i< totalNode; i++){
     
        int min = 10000000;
        int index = -1;
        
        
        for( int j=0 ; j<totalNode; j++){
            if( visit[nodeArr[j]] == false && min > dist[nodeArr[j]]  ){
                min = dist[nodeArr[j]];
                index= nodeArr[j];
            }
        }
        //cout<< index<<" index"<<endl;
        visit[index] = true;
        
        for(int k =0;  k< totalNode; k++){
            //cout <<distArr[index][nodeArr[k]] <<" "<<dist[nodeArr[k]] <<" "<<dist[index] + distArr[index][nodeArr[k]]<<endl;
            
            if( distArr[index][nodeArr[k]] != 0 && dist[nodeArr[k]] > dist[index] + distArr[index][nodeArr[k]] +degreeArr[index] ){
                //cout<<index<<" "<<nodeArr[k]<<" "<<dist[index] <<" "<<distArr[index][nodeArr[k]]<<endl;;
                dist[nodeArr[k]] =dist[index] +distArr[index][nodeArr[k]];
                if( index != (int)c -97){
                    dist[nodeArr[k]]+= degreeArr[index];
                }
              //  cout<< nodeArr[k]<<":"<<dist[nodeArr[k]] <<" "<<dist[index] +distArr[index][nodeArr[k]]<<" "<<degreeArr[index]<<endl;
;
            }
        }
        
        
    
    }
}


int bigestNode( int a, int b, int c){
    if( a> b){
        if( a>c){
            return a;
        }
        else{
            return c;
        }
    }
    else{
        if( b>c){
            return b;
        }
        else{
            return c;
        }
    }
}


int main(void) {
    
    input >> totalNode;
    char friends[3];
    for( int i=0; i<3; i++){
        input>> friends[i];
    }
    
    nodeArr = new int[totalNode];
    degreeArr= new int[26];
    
    for( int i=0; i< totalNode; i++){
        for( int j=0; j<totalNode; j++){
            distArr[i][j] =0;
        }
    }

    
    for( int i=0; i<totalNode; i++){
        int inputnumber;
        char fV;
        input>> fV>>inputnumber ;
        nodeArr[i]= (int)fV -97;
        degreeArr[(int)fV -97]= inputnumber;
        for( int j=0; j< inputnumber; j++){
            char tV;
            int dist ;
            input>> tV >>dist;
            distArr[(int)fV -97][ (int)tV-97] =dist;
        }
    }
    
    int friendroute1[26];
    int friendroute2[26];
    int friendroute3[26];
    for( int i=0 ; i<26;i++){
        friendroute1[i] =100000;
        friendroute2[i] =100000;
        friendroute3[i] =100000;
    }
    
    dijkstra(friends[0],friendroute1);
    dijkstra(friends[1],friendroute2);
    dijkstra(friends[2],friendroute3);
    
    int min=10000;
    int tempNode= 10000;
    int resultIndex =0;
    for( int i=0; i< totalNode ; i++){
        
        tempNode= bigestNode(friendroute1[ nodeArr[i]],friendroute2[ nodeArr[i]],friendroute3[ nodeArr[i]] );
        
            
    
        if( tempNode < min ){
            min = tempNode;
            resultIndex= nodeArr[i];
        }
        
    }
    output<<(char)(resultIndex+97)<<" "<< min<<endl;
    return 0;
}
