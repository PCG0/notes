#include <bits/stdc++.h>
using namespace std;


char opt;
void xiaoluo(char opt)
{
	switch(opt)
	{
		case 'G':cout<<"Hello,my master!"<<endl;
		case 'N':cout<<"I'm Xiaoluo"<<endl;break;
		case 'S':cout<<"Teinei teinei~"<<endl;break;
		case 'B':case 'Q':
			cout<<"Bye bye!"<<endl;
			exit(100);
			break;
		default:cout<<"Sorry..."<<endl;
	}
}

int main(int argc, char const *argv[])
{
	while(true)
	{
		cin>>opt;
		xiaoluo(opt);
	}
	return 0;
}