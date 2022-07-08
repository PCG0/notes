#include <cstdio>
#include <cstdlib>
#include <windows.h>
#include <process.h>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

char inputCode[32];

int main()
{
	SetConsoleOutputCP(65001);// 中文显示支持

	cout << R"(====>> Resu's Bot 简体中文 v0.0.1 Beta <<====
嗨。许久未见，bot现已使用 C++ 编写！

命令列表
null

)";
	//scanf("%d",&inputCode);
	cout << ">>";
	cin >> inputCode;
	

	system("pause");
}