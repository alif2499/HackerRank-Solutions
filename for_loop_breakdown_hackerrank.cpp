

#include <iostream>
#include<bits/stdc++.h>
#include <cstdio>
using namespace std;

int main(){
    // Complete the code.
    int a,b;
    string arr[9] = {"one","two","three","four","five","six","seven","eight","nine"};
    cin>>a>>b;
    for (int i = a; i<=b ; i++){
        if (i<=9){
            cout<<(arr[i-1])<<endl;
        }
        else if(i>9 && i % 2 == 0){
            printf("even\n");
        }
        else if(i>9 && i%2!=0){
            printf("odd\n");
        }
    }
    return 0;
}


