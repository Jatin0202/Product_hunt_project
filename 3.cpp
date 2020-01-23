#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		srting a;
		cin>>a;
		int len=a.length();
		cout<<len;
		if(a[len-1]=='o')
			cout<<"FILIPINO"<<endl;
		else if(a[len-1]=='u')
			cout<<"JAPANESE"<<endl;
		else if(a[len-1]=='a')
			cout<<"KOREAN"<<endl;
	}
}
