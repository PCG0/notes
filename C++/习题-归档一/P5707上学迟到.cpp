#include <bits/stdc++.h>

int main(int argc, char const *argv[])
{
	int s, v;
	scanf("%d%d", &s, &v);
	int t_walk=ceil(1.0*s/v)+10
		, from_zero=60*(24+8)-t_walk
		, hh=(from_zero/60)%24
		, mm=from_zero%60;
	printf("%02d:%02d", hh, mm);
	return 0;
}