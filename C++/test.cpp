#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
  float a;// 输入
  int A = 2;// 步长
  int b = 0;// 输出
  cin >> a;
  do
  {
    b++;
    //A = A + A*0.98;
    A *= 0.98;
    a -= A;   
    cout << b << endl << a << endl;
  }
  while (a - A >= 0);
  
}