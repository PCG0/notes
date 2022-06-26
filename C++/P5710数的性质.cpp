// #include <iostream>
// using namespace std;

// int a, A, Uim, Ba, Zm;
// int main()
// {
// 	cin >> a;
// 	if (4<=a && a<=12)
// 	{
// 		if (a%2 == 0) {A++; Uim++;}
// 		else Ba++;
// 	}	
// 	else Zm++;
// 	cout << A << ' ' << Uim << ' ' << Ba << ' ' << Zm;
// }

#include <bits/stdc++.h>

int main(int argc, char const *argv[])
{
	int x; bool p1, p2;
	std::cin>>x;
	p1=x%2==0;
	p2=4<x&&x<=12;
	printf("%d %d %d %d"
		, (p1&&p2)
		, (p1||p2)
		, (p1^p2)
		, !(p1||p2)
	);
	return 0;
}