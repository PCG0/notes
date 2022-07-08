#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    // 在许多 Online Judge 评测中，编译时会定义 ONLINE_JUDGE 宏。
    // 如果有检测到这个宏，就不会运行重定向操作。
    #ifndef ONLINE_JUDGE
        // 这是重定向到输入输出文件的语句
        freopen("C++\\title.in", "r", stdin);
        freopen("C++\\title.out", "w", stdout);
    #endif
    string s;
    int ans = 0;
    while (cin >> s)
        ans += s.length();
    cout << ans << endl;

    return 0;
}
