#include <iostream>
using namespace std; 

long long fact(long long n){
    return 
        ((n == 1) ?
         1
         :
         fact(n-1) * n);
}

long long fib(long long n){
    return
        ((n <= 1) ?
         n
         :
         fib(n-1) + fib(n-2));
}

int main(void){
    cout << fact(4) << endl;
    cout << fib(17) << endl; // 1597
    return 0;
}

