#include <bits/stdc++.h>

void userName(char _userName,int _userSalt)
{
    // 打开目标文件
    freopen("user.out","a",stdout);
    // 存入
    std::cout
        <<_userName<<std::endl
        <<_userSalt<<std::endl;
    
}

int main(int argc, char const *argv[])
{
    char name;
    const int salt = 123;
    std::cin>>name;
    userName(name,salt);
    return 0;
}
