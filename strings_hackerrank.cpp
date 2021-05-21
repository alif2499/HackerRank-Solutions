

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin>>a>>b;
    char temp;
    int aLength = a.size();
    int bLength = b.size();
    char a0 = a[0];
    char b0 = b[0];
 
    cout<<aLength<<" "<<bLength<<endl;
    cout<<a+b<<endl;
    temp=a[0];
    a[0]=b[0];
    b[0]=temp;
    cout<<a<<" "<<b<<endl;
  
    return 0;
}

