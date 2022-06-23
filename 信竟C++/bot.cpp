#include <cstdio>
#include <cstdlib>
#include <windows.h>
#include <process.h>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int mp[100][100];
int last[100];
int n = 22, m = 62;
//char inputCode;

void draw(int x1, int y1, int x2, int y2, char ch = '#'){
    for(int i = x1; i <= x2; i++)
        for(int j = y1; j <= y2; j++)
            mp[i][j] = ch;
}
// void draw(int x1, int y1, char ch = '#') draw(x1, y1, x1, y1, ch);

void drawman(int x, int y){
    draw(x, y+5, x, y+12, '*'); x++;
    draw(x, y+4, x, y+15, '*'); x++;
    draw(x, y+4, x, y+7); draw(x, y+8, x, y+13, '.'); draw(x, y+12); x++;
    draw(x, y+2, x, y+14); draw(x, y+3, x, y+4, '.');
    draw(x, y+8, x, y+12, '.'); draw(x, y+15, x, y+18, '.'); x++;
    draw(x, y+2, x, y+17); draw(x, y+5, x, y+11, '.'); x++;
    draw(x, y+5, x, y+15, '.'); x++;
    draw(x, y+4, x, y+13); draw(x, y+6, '*'); x++;
    draw(x, y+1, x, y+17); draw(x, y+5, x, y+11, '*'); x++;
    draw(x, y, x+2, y+20, '.'); draw(x, y+4, x+2, y+16, '*');
    draw(x, y+3); draw(x, y+14, x+1, y+16); draw(x+1, y+16, '.');
    draw(x+2, y+8, x+2, y+11, ' '); draw(x, y+7, '.'); draw(x, y+12, '.');
    draw(x+3, y, x+4, y+19); draw(x+3, y+6, x+4, y+13, ' ');
    draw(x+3, y, x+3, y+1, ' '); draw(x+3, y+18, x+3, y+19, ' ');
}

// 打印输出
void printscreen(){
    for(int i = 1; i <= n; i++){
        last[i] = m;
        while(mp[i][last[i]] == ' ')
            last[i]--;
    }
    for(int i = 1; i <= n; i++,puts(""))
        for(int j = 1; j <= last[i]; j++)
            putchar(mp[i][j]);
}

int main()
{
	SetConsoleOutputCP(65001);// 中文显示支持

	for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
            mp[i][j] = ' ';
    drawman(1, 2);
    printscreen();

    return 0;
// 	cout << R"(====>> Resu's Bot 简体中文 v0.0.1 Beta <<====
// 嗨。许久未见，bot现已使用 C++ 编写！

// 命令列表
// null

// )";
// 	//scanf("%d",&inputCode);
// 	cout << ">>";
// 	cin >> inputCode;


	//system("pause");
}