#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    freopen("C++/2/三角形输出.in","r",stdin);
    freopen("C++/2/三角形输出,out","w",stdout);
    int n; 
    cin>>n;
    for(int i=1; i<=n; ++i)
    {
        // string(int a,char b)
        string space = string(n-i,' ');
        string ch = string(2*i-1,'A'+i-1);
        cout<<space+ch<<endl;
    }
    return 0;
}
