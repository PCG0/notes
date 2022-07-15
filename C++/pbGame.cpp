// P3150 pb的游戏（1）

#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    #ifndef ONLINE_JUDGE
        freopen("C++\\pbGame.in","r",stdin);
        freopen("C++\\pbGame.out","w",stdout);
    #endif
    int n,index[51];
    cin>>n;
    for(int i=1; i<=n; ++i)
    {
        cin>>index[i];
        // 这句话等效与if (a & 1 == 1)还有if (a % 2)以及if (a % 2 == 1)因为所除的数2是2的1次幂，
        // 可以使用位运算加快速度，简化书写
        // if(index[i] & 1)
        //     cout<<"zs wins"<<endl;
        // else
        //     cout<<"pb wins"<<endl;

        
        cout<<(index[i]&1?"zs wins":"pb wins")<<endl;
        // a?b:c
        // 三目运算符，相当于：
        // if(a==1)return b;
        // else return c;
            
    }
        
    return 0;
}
