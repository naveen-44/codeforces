#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
  long long n,m,a;cin>>n>>m>>a;
  long long x1,x2;
  	x1=n/a;
  	x2=m/a;
  if(n%a!=0){
  	x1++;
  }
  if(m%a!=0){
  	x2++;
  }
  cout<<x1*x2;
}
