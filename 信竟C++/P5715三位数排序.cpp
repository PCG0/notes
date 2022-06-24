#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int ip[3];
	for (int i=0;i<3;i++) cin>>ip[i];
	sort(ip, ip+3);
	for (int i=0;i<3;i++) cout<<ip[i]<<" ";
	return 0;
}

// #include <bits/stdc++.h>
// using namespace std;

// int main(int argc, char const *argv[])
// {
// 	int ip[1100];
// 	for (int i=1;i<=3;i++) cin>>ip[i];
// 	sort(ip+1, ip+3+1);
// 	for (int i=1;i<=3;i++) cout<<ip[i]<<" ";
// 	return 0;
// }