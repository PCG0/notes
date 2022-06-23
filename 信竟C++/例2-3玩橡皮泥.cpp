#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	const double PI=3.141593;
	int r1=4, r2=10;
	double V, l;
	V=4.0/3*PI*(pow(r1,3)+pow(r2,3));// 不能写成4/3
	l=pow(V, 1.0/3);// 不能写成1/3
	cout<<int(l)<<endl;// 强制类型转换，比如double()就是强制转换成双精度浮点类型 
	return 0;
}