#include <bits/stdc++.h>
using namespace std;

class Person
{

public:
    string name;
    int age;
    char gander;

    Person(){};
    Person(string name)
    {
        this->name = name;
        cout<<this->name<<"已出生"<<endl;
    }
    ~Person(){cout<<this->name<<"已死亡."<<endl;};

    

};

int main(int argc, char const *argv[])
{
    // freopen("C++\\pbGame.in","r",stdin);
    freopen("C++\\world.out","w",stdout);

    Person* human_1 = new Person("hhh");
    return 0;
}
