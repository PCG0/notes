#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    //  制作一张九九乘法表。
    // freopen("C++\\99.out","w",stdout);
    for(int i=1; i<=9; i++)
    {   for(int j=1; j<=9; j++)
            printf("%d*%d=%d    ",j,i,i*j);
        cout<<endl;
    }


    return 0;
}
