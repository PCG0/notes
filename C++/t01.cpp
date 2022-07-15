#include <bits/stdc++.h>
using namespace std;

char s1[1005], s2[1005];
int main(int argc, char const *argv[])
{
    fgets(s1, 1004, stdin);
    fgets(s2, 1004, stdin);
    // 这里需要减一是因为 fgets 会吃进一个换行符
    int len1 = strlen(s1)-1, len2 = strlen(s2)-1, ans;
    for(int i=1; i+len2-1<len1; i++)
    {
        bool matched = true;
        for(int j=0; j<len2; j++)
        {
            if(s1[i+j] !=s2[j])
            {
                matched = false;
                break;
            }
        }
        if(matched)
        {
            ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
}
