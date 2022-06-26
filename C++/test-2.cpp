#include <windows.h>
#include <bits/stdc++.h>
using namespace std;

SYSTEMTIME sys; 
int main(int argc, char const *argv[])
{
	while (true)
	{
		GetLocalTime(&sys);
		printf("%4d-%02d-%02d %02d:%02d:%02d\n"
			, sys.wYear
			, sys.wMonth
			, sys.wDay
			, sys.wHour
			, sys.wMinute
			, sys.wSecond
			);
		Sleep(200);
		system("cls");
	}
	return 0;
}