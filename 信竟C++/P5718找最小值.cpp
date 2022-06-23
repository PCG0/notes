#include <bits/stdc++.h>
using namespace std;

int x, y[1100];
int main()
{
	
	cin >> x;
	for (int i=0; i<x; i++) cin >> y[i];
	cout << *min_element(y, y+x);
	return 0;
}