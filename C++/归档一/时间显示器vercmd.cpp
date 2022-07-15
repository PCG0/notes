#include <windows.h>
#include <bits/stdc++.h>
using namespace std;

SYSTEMTIME sys; 
int main(int argc, char const *argv[])
{
	SetConsoleOutputCP(65001);
	while(true)
	{
		// 输出时间
		GetLocalTime(&sys);
		string week[7] = { "星期日","星期一","星期二","星期三","星期四","星期五","星期六" };
		printf("现在的系统时间：\n\n	%02d:%02d:%02d\n\n 		%4d年%02d月%02d日"
			, sys.wHour
			, sys.wMinute
			, sys.wSecond
			, sys.wYear
			, sys.wMonth
			, sys.wDay
			);
		cout<<week[sys.wDayOfWeek]<<endl<<endl<<endl;
		
		// 倒计时条
		int counts = 60-sys.wSecond
			, countm = 60-sys.wMinute
			, counth = 24-sys.wHour;

		cout<<"[";
		for (int i=0; i<counth; i++) cout<<"=";
		for (int i=0; i<=sys.wHour; i++) cout<<" ";
		cout<<"]时\n";

		cout<<"[";
		for (int i=0; i<countm; i++) cout<<"=";
		for (int i=0; i<=sys.wMinute; i++) cout<<" ";
		cout<<"]分\n";

		cout<<"[";
		for (int i=0; i<counts; i++) cout<<"=";
		for (int i=0; i<=sys.wSecond; i++) cout<<" ";
		cout<<"]秒\n";

		

		// 保证有1000ms的延迟
		Sleep(1000);
		system("cls");
	}
	return 0;
}