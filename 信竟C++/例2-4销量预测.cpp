#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	double a=1, b=-100, c=2400, delta, ans;
	delta=pow(b,2)-4*a*c;
	ans=(-b+sqrt(delta))/(2*a);
	cout<<110-int(ans+0.5)<<endl;
	return 0;
}