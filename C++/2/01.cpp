#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int sac = 0, n;
    cin>>n;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= n-i+1; j++)
            printf("%02d", ++sac);
        printf("\n");
    }
    return 0;
}
