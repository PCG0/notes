#include <bits/stdc++.h>
using namespace std;

class person
{
public:
    string name;

    person(){};
    person(string name)
    {
        this->name=name;
    };
    ~person()
    {
        cout<<this->name<<" 已死亡。"<<endl;
    };

};

int main(void)
{
    //  创建人物，程序结束时自动删除
    person p1("resu");
    person p2("rrection");
    return 0;
}
