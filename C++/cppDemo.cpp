#include <bits/stdc++.h>

// 使用 using namespace 避免混淆重名变量或方法，默认指向 using 的 namespace
using namespace std;

// namespace 这个方式声明了一块命名空间
namespace mySpace
{
    int a;
    int b;
}
// :: 作用域符号

// 这是一个人类
class Person
{
    // 三个作用域，只探讨其中两个
    // private 私有修饰符
    // public 公开修饰符
    // this 关键字，代表对象本体，可以不写
// 无法直接调用，很安全
private:
    // 小名
    string smallName;
    // 年龄
    int age;
    // 性别
    char gander;

public:
    // 名字
    string name;

    // Person 的无参构造函数
    Person(){};
    // Person 的有参构造函数
    Person(string name)
    {
        this->name = name;
    };
    // 至于这里要把无参写上，是因为写了有参之后就不自动写无参了，所以要写无参

    void eat()
    {
        cout << name << "正在吃饭" << endl;
    }

    //  可以间接调用 private

    void setSmallName(string name)
    {
        // 使用 this 关键字避免混淆
        this->smallName = name;
    }

    string getSmallName()
    {
        // this 关键字是会变动的
        return this->smallName;
    }

    // 类里的函数叫方法，变量叫属性

    // static
    static int aa;
    // 因为生命周期比较长，而且比较早（与类同时生成），所以导致一个问题
    // 不可以被直接调用
    // 还没等类实例化，static 修饰的属性就已经诞生了
    // static 修饰的东西属于类本身，仅有一个
    // 既然 static 是修饰符，那么 static 也能用来修饰函数！

    static void staticAa()
    {
        // static 修饰的函数是否能够调用非 static 属性？
        // 尝试一下：
        // this.name = "hh";
        // 结论：非 static 的属性和方法都不能写到 static 修饰的方法里
        cout<<aa<<endl;
        // 只能调用 static 修饰的东西
    }
};

class Animal
{
    // 构造函数用来构造对象

    // 理论上新建的类里是空的，但实际上存在一个我们看不见的函数，它叫：无参构造函数
public:
    Animal()
    {
        // 没有报错。证明了类确实存在无参构造函数
        // 它没有返回值类型、没有参数
        // 它的代码在哪？也是看不见的
    }

    // 为什么要有无参构造函数？
    // 它是用来构造函数的，所以我们能够实例化对象归功于无参构造函数
    // Person* p = new Person(); 中加括号是为了调用无参构造函数
    // 因此，无参构造函数十分重要

    // 那么有没有“有参构造函数”？——有的。
    // string name;
    // Animal(string name)
    // {
    //     this->name = name;
    // }
    // 用来初始化
};

// 瞎猫碰死耗子
int Person::aa = 10;

int main(int argc, char const *argv[])
{
    int a = 20;
    mySpace::a = 10;
    // 就近原则
    cout<<a<<endl;
    cout<<mySpace::a<<endl;

    // 有两种方式，一个用 new 操作符，一个是直接声明一个变量

    // 指针变量的形式
    Person* p = new Person();

    // 用string创建出来的变量都可以用“.”
    // “.”指该对象包含的内容

    // 如果一个变量是指针变量就不能用“.”调用，而是“->”调用
    // 因为要进行区分

    p->name = "Resu";

    cout<<p->name<<endl;

    p->eat();

    // ∵string.size() string.replace() 都是方法
    // ∴string 是一个类

    // 第二种实例化对象的方式

    Person p1;
    p1.name = "我是以变量的方式直接声明的，直接实例化的对象";
    p1.setSmallName("小R");
    cout<<p1.getSmallName() << endl;
    cout<<p1.name<<endl;

    // p1.aa = 10;
    // 上面这条代码没有报错，但不能运行
    // 尝试另外一种方式：
    // Person::aa = 10;
    // 这样也是不行的
    // 如果想要给 Person::aa 赋值，则需要全局赋值，即在 int main() 函数外赋值
    cout<<Person::aa<<endl;

    // 特殊：static 修饰的方法是可以被对象调用的
    p1.staticAa();

    // 无参
    Person* p2 = new Person("human");
    cout<<p2->name<<endl;

    return 0;
}
// 这些玩法是面向对象的三大特性之一：封装性