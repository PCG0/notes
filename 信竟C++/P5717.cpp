#include <iostream>
using namespace std;

int a, A, Uim, Ba, Zm;
int main()
{
	cin >> a;
	if (4<=a && a<=12)
	{
		if (a%2 == 0) {A++; Uim++;}
		else Ba++;
	}	
	else Zm++;
	// cout << A << ' ' << Uim << ' ' << Ba << ' ' << Zm;
	printf("%d %d %d %d", A, Uim, Ba, Zm);
	return 0;
}

// #include <iostream>
// #include <cstdio>
// #include <algorithm>
// #include <cstring>
// using namespace std;
// int x;
// bool a, b;
// int main(){
// 	scanf("%d", &x);
// 	a = !(x & 1), b = (x > 4 && x <= 12);//a满足性质1，b满足性质2
// 	printf("%d %d %d %d", a & b, a | b, (a && !b || b && !a), !a && !b);
//    //按条件输出就好啦QWQ
// }