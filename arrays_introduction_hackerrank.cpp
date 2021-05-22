

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int arr[1000];
    int a;
    cin>>a;
    for (int i=0;i<a;i++){
        cin>>arr[i];
    }
    for (int i=a-1;i>=0;i--){
        cout<<arr[i]<<" ";
    }   
    return 0;
}

