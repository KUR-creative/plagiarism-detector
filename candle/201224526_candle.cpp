#include <iostream>
#include <fstream>

using namespace std;

class candle{
private:
    int total;
    char member[3];
    int node_list[30];
    int node_num[30];
    int link_list[30][30];
    int link_num[30][30];
    int before[30][30];
    int degree[1000];
public:
    void get_info();
    void search_shortest();
};
void candle::get_info(){
    ifstream infile("candle.inp");
    int get_num;
    char get_cha;

    infile >> total ;
    infile >> member[0] >> member[1] >> member[2];
    for(int i = 0 ; i< total ; i++)
            for(int j = 0 ; j < total ; j++)
                link_num[i][j] = 99999;

    for(int i = 0; i < total ; i++){
        infile >> get_cha >> get_num;
        node_list[i] = get_cha - 97;
        node_num[i] = get_num;
        degree[get_cha - 97] = get_num;
        for(int j = 0; j < node_num[i]; j++){
            infile >> get_cha >> get_num;
            link_num[node_list[i]][get_cha-97] = get_num;
        }
    }
    for(int i = 0 ; i< total ; i++){
        for(int j = 0 ; j < total ; j++){
            before[i][j] = i;
        }
    }


     for(int i = 0 ; i< total ; i++){
            cout << char(i+97) << " " << degree[i] << " : " ;
            for(int j = 0 ; j < total ; j++){
                cout << link_num[i][j] <<" ";
            }
            cout << endl;
     }
}
void candle::search_shortest(){
        ofstream outfile("candle.out");

    for (int k = 0; k < total; k++){
        for (int i = 0; i < total; i++){
            for (int j = 0; j < total; j++){
                if (link_num[i][j] > link_num[i][k] + link_num[k][j] + degree[k]){
                    link_num[i][j] = link_num[i][k] + link_num[k][j] + degree[k];
                //    before[i][j] = before[k][j];
                }
            }
        }
    }
    cout << endl;
    for(int i = 0 ; i< total ; i++){
            cout << char(i+97) << " " << degree[i] << " : " ;
            for(int j = 0 ; j < total ; j++){
                cout << link_num[i][j] <<" ";
            }
            cout << endl;
     }
    int min_des = 999999;
    char min_cha;
    for(int i =0; i < total ; i++){
        if( min_des > max(max(link_num[member[0]-97][i],link_num[member[1]-97][i]),max(link_num[member[0]-97][i],link_num[member[2]-97][i])) ){
            min_des = max(max(link_num[member[0]-97][i],link_num[member[1]-97][i]),max(link_num[member[0]-97][i],link_num[member[2]-97][i]));
            min_cha = i+97 ;
        }
        else if ( min_des == max(max(link_num[member[0]-97][i],link_num[member[1]-97][i]),max(link_num[member[0]-97][i],link_num[member[2]-97][i])) ){
            if(min_cha > i){
                min_cha = i+97 ;
            }
        }
    }
    cout << member[0] << " " << member[1] << " " << member[2] << endl;
    outfile << min_cha << " " << min_des;


}
int main()
{
    candle A;
    A.get_info();
    A.search_shortest();

}
