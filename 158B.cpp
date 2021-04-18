#include <bits/stdc++.h>
#include<cstring>
using namespace std;

int main() {
	int n;
	cin>>n;
	int a[5]={0},x;
	for(int i=0;i<n;i++){
		cin>>x;
		a[x]++;
	}
	int sum=0,val,a3=0,a2=0,a1=0;
	sum+=a[4];
	a3=a[3];
	a2=a[2];
	a1=a[1];
	if(a3<=a1){
		sum+=a3;
		a1-=a3;
	}
	else{
		sum+=a3;
		a1=0;
		a3=0;
	}
	sum+=a2/2;
	a2=a2%2;
	if(a2!=0)a1+=2;
	sum+=(a1/4);
	a1=a1%4;
	if(a1!=0)sum+=1;
	cout<<sum;
return 0;	
}
