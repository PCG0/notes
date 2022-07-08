#include <iostream>
using namespace std;

int a, b, c, d;
int main(){
	cin >> a >> b >> c >> d;
	if (b >= d){
		d += 60;
		c--;
		d -= b;
	}
	else d -= b;
	c -= a;
	printf("%d %d", c, d);
	return 0;
}