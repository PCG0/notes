// 这是一个万能头文件，包含了大多数头文件
// 这是 C++ 封装好的数据结构（STL）
#include <bits/stdc++.h>

// 数组是最简单的数据结构：数组是存同样类型的数据串、数据序列的

// 使用 using namespace 避免混淆重名变量或方法，默认指向 using 的 namespace
using namespace std;

// namespace 这个方式声明了一块命名空间 
// :: 作用域符号 
namespace mySpace
{
    int a;
    int b;
}

namespace tempc
{
    int a,b;
}

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
    // 秘密资料
    string dontLookThis;

public:
    // 名字
    string name;
    // 年龄
    int age;
    // 性别
    char gander;

    // 构造函数用来构造对象
    // 理论上新建的类里是空的，但实际上存在一个我们看不见的函数，它叫：无参构造函数

    // Person 的无参构造函数
    Person(){};
    // Person 的有参构造函数
    Person(string name)
    {
        this->name = name;
    };
    // 至于这里要把无参写上，是因为写了有参之后就不自动写无参了，所以要写无参

    // 这是一个析构函数，用来释放内存
    ~Person()
    {
        cout<<this->name<<" 被杀死了，原因不明"<<endl;
    };

    // 初始化列表
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

// 这是一个动物
class Animal
{
public:
    Animal()
    {
        // 没有报错。证明了类确实存在无参构造函数
        // 它没有返回值类型、没有参数
        // 它的代码在哪？也是看不见的
    }

    ~Animal(){};

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

// 结构体
struct abc
{
    // 结构体与类的唯一区别在于没有作用域的修饰符，默认 public，只能写属性和构造函数
    // 不能写函数
    int a;
    int b;
    // 其实写构造函数也是违规的，它是引入了 C++ 的特性
    abc(){};

    // 初始化列表
    abc(int a, int b):a(a),b(b){};

};

// 数组如何作为一个返回值去定义一个函数
int* getArr()


{
    // 最好用 new 创建数组
    // 否则一旦调用完这个函数，里面的变量便会自动销毁
    // delete[]
    int* arr = new int[5];
    for(int i=0; i<5; i++)
        arr[i] = i;
        // 在堆上
    return arr;
}

// 模板化与泛型
// 泛型就是通用类型或广泛类型，不先确定一个类型
// 声明一个 T 这样的通用类型（泛型）
// 如何使用？放到函数的上面就可以了
template<class T>
bool maxA(T a, T b){return a > b;}

// 也可以对函数定义一个泛型：
template<class C>
class Machine
{
public:
    C data;
    Machine(){}
    ~Machine(){}
    Machine(C data)
    {
        cout<<data<<endl;
    }
};

void Strh()
{
    // C 字符串

    // 这是一个字符串
    // 末尾的 \0 是结束标识符，属于代码规范，必写
    char strArr[] = {'a','b','c','\0'};
    cout<<strArr<<endl;
    // 字符数组有自己的初始化方式：
    // 如果是这种方式，会默认在末尾加 \0
    char str[] = "Hello world";
    cout<<str<<endl;

    // 当我们使用 scanf 或 cin 录入数据时，往往空格后面的数据就不录入了
    // 用下面的方法解决：
    // gets(字符数组);
    // cin.getline(字符数组,长度);
    // fgets(字符数组,长度,stdin);      它不光录入空格还录入回车 \n

    // 不借助 for 循环下标法从 strArr 的下标2开始输出
    cout<<strArr+2<<endl;
    // 原理：字符数组可以根据内存地址直接从头到尾输出
    
    // string.h
    // strlen();    返回字符串的长度，不接收\0
    // strcmp();    以字典排序方式比较字符串大小
    // strcpy();    拷贝
    // strcat();    追加
}

void CppStr()// C++ 字符串
{
    // 有一个类型的题目是找到输出图形的规律，然后将其实现。
    // 观察下面的图形。你想想该如何输出呢？
    //  A
    // BBB
    cout<<" A"<<endl
        <<"BBB"<<endl;
    // 那么对于：
    //   A
    //  BBB
    // CCCCC
    // 同理：
    cout<<"  A"<<endl
        <<" BBB"<<endl
        <<"CCCCC"<<endl;


    // C++ 字符串是一个新的类型：string
    // string 是特殊的数据结构，是 STL 容器中的一员
    // 有如下三种初始化方式
    string s1 = "hello world";
    cout<<s1<<endl;

    string s2(5,'a');
    cout<<s2<<endl;

    string s3("three");
    cout<<s3<<endl;

    // ∵ string 使用“+”拼接：
    // s1 = s1+"!";
    // ∴ 也能在前面拼接：
    // s1 = "pre "+s1;
    // 综上，
    s1 = "pre "+s1+"!";
    // string 类型只支持 cin 和 cout
    cout<<s1<<endl;

    // replace()    替换
    string s4 = "123456";
    cout<<s4<<endl;
    // 参数一表示被替换的字符串的起始下标，参数二表示要替换的范围（这里提供3，就是要把345替换掉）
    // 参数三表示要用来替换的字符串，参数四、五同理参数一、二
    s4.replace(2,3,"ABCD",2,2); // 12CD6
    cout<<s4<<endl;
    // 如果想要把 ABCD 全替换上去：
    s4.replace(2,3,"ABCD"); // 12ABCD
    cout<<s4<<endl;

    // erase.(起始位置,长度)    擦除
    // 从下标4的位置开始擦除
    s4.erase(4); //12AB
    cout<<s4<<endl;

    // ∵ string 的底层也是字符数组
    // ∴ 也能使用下标法
    cout<<s4[1]<<endl;
    // ∴ 也能修改其单个元素：
    s4[1] = 'A';
    cout<<s4<<endl;

    // string 也可以比较大小，且比字符数组更为简单，真是惊呆了
    string strA = "123";
    string strB = "345";
    if(strA > strB)
        cout<<strA<<">"<<strB<<endl;
    else if(strA == strB)
        cout<<strA<<"="<<strB<<endl;
    else
        cout<<strA<<"<"<<strB<<endl;

    // 字符数组和 string 的转换：
    char hh[] = "hh";
    string www = hh; //字符数组转变为 string 类型
    // string 是没法直接转为字符数组的，只能转为 const char[]
    char* w = (char*)www.c_str();
    cout<<w<<endl;
}

void Sstream()
{
    // 建立一个字符串的输入流
    string src("hello 123 4.5 T");
    istringstream is(src);

    string s1;
    int a;
    double b;
    char c;

    is>>s1>>a>>b>>c;
    
    cout<<s1<<endl
        <<a<<endl;

    // 输出流
    ostringstream os;
    os<<s1<<"哈哈"<<a<<" "<<b<<" "<<c<<endl;
    cout<<os.str()<<endl;
}

// 瞎猫碰死耗子
int Person::aa = 10;

// 可扩展的一个数组，它的底层就是数组
vector<int> v;
// map 的实现原理是 红黑树
// 它必须要提供两个类型,因为它是"大名鼎鼎"的键值对结构
// 有一种数据形式非常受欢迎,而且很符合人的逻辑思维
// 叫做 键值对
// 例如 json 数据传输和反馈, json 就是键值对形式
// arr[0] = val 下标 == key
// map 可以自定义 key 的类型
// 还有一个 unordered_map,无序的 map,查找效率要比 map 更加的高
// 原理是 哈希表
map<string,int> m;

// 指针是否能作为函数的返回值？
// 可以的
// 这个操作叫：传址
void f(int *a,int *b)// 用指针来找到内存单元实现交换
{
    int temp = *a;
    *a = *b;
    *b = temp;
    // 实参和形参的内存地址是一样的
    // 那么我们就可以根据一样的内存地址找到同一个内存空间
}

// 主程序
int main(int argc, char const *argv[])
{
    // 宏定义，上传到洛谷等大多数 Online Judge 时忽略该宏
    #ifndef ONLINE_JUDGE
        // 重定向。将输出存入 .out 文件中
        freopen("C++\\cppDemo.out","w",stdout);
    #endif

// C 字符串
    Strh();

// C++ 字符串
    CppStr();

// string stream 字符串流
    Sstream();

// 函数、类、static
    int a = 20;
    mySpace::a = 10;
    // 就近原则
    cout<<a<<endl;
    cout<<mySpace::a<<endl;

    // 有两种方式，一个用 new 操作符，一个是直接声明一个变量

    // 指针变量的形式。类的类型叫引用类型
    Person* p = new Person();

    // 用string创建出来的变量都可以用“.”
    // “.”指该对象包含的内容

    // 如果一个变量是指针变量就不能用“.”调用，而是“->”调用
    // 因为要进行区分

    p->name = "Resu";

    cout<<p->name<<endl;

    p->eat();

    // ∵ string.size() string.replace() 都是方法
    // ∴ string 是一个类

    // 第二种实例化对象的方式

    Person p1;
    // 不知道为什么以变量直接声明，程序结束后即使我没 delete 它也会释放
    p1.name = "我是以变量的方式直接声明的，直接实例化的对象";
    p1.setSmallName("小R");
    cout<<p1.getSmallName()<<endl;
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

    // new 调用不可见的无参构造函数，实例化一个对象
    Person* p2 = new Person("human");
    cout<<p2->name<<endl;

    // 这些玩法是面向对象的三大特性之一：封装性

 // 析构函数
    // 不用 new 操作符创建的东西，可能关闭程序后自己就释放了
    // 用 new 创建的东西是不会自己释放的
    // delete 之所以能释放内存，是因为调用了不可见的析构函数
    delete p2;
    // 建立了一个非常大的数组，它太消耗内存了
    int* arr = new int[100005];
    // 因为 new 是不会自己释放的，所以我们后边要用 delete 释放它
    // 面对数组，要用 delete[]
    delete[] arr;// 这里已经释放掉了,没输出而已

// 指针
    // 指针是一种特殊的复合类型
    // 因为指针它是这样写的：基本类型/引用类型 *
    // 指针变量是用来存储内存地址的
    // int* arr = new int[100];
    // 之所以用指针变量来存储 new
    // 是因为 new 完的对象返回的是一个内存地址

    // “指针存储的内存地址，用解引用的方式可以直接对这块连续的内存单元进行操作”
    // 不要小瞧上边这段话，这个功能足够去做外挂或反汇编了
    // 它代表的就是连续的内存单元本体
    (*p).age = 10;
    // 当我们拿到了一个内存地址，通过解引用去修改里面的值
    // 例如植物大战僵尸里面，如果我们找到了阳光这个变量的内存地址
    // 然后我们去用
    // int* p = 阳光变量的内存地;
    // *p = 500;
    // 那么阳光的值就会变成 500！
    cout<<(*p).age<<endl
        <<p->age<<endl;
    int ta{100};
    int* lp = &ta;
    cout<<lp<<endl
        <<&ta<<endl
        <<&lp<<endl
        <<*lp<<endl // 解引用
    ;

    // 数组是不是一个连续的内存空间？
    int* getarr = getArr();
    for(int i=0; i<5; i++)
        cout<<getarr[i]<<endl;

// 模板化与泛型
    // 它是如何确定类型的？
    // 如果我们提供的数据是可以明确类型的话
    // T 就会自动转换
    cout<<maxA(19,20)<<endl
        <<maxA('a','b')<<endl
        <<maxA(20.6,10.0)<<endl;
    // 我们也可以直接指定类型：
    cout<<maxA<int>(10,20)<<endl;

    // 模块化类：
    Machine<string> *bot = new Machine<string>("Resu");
    // 也可以这样去声明：
    Machine<int> bot2;
    bot2.data = 100;
    cout<<bot->data<<endl; 
    cout<<bot2.data<<endl;

// STL vector、unique去重
    // 容量不够大的时候，自动扩容
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    cout<<v.size()<<endl;

    // resize() 重新定义矢量表的长度

    // pop 弹出最后一个元素 pop_back()
    v.pop_back();
    
    // 此时用for历遍出来的只有3个：
    for(int i=0; i<v.size(); ++i)
        cout<<v[i]<<endl;
    // 显然，向上面那样写太过于麻烦了，我们可以用 for each 来偷工减料：
    // for each 要遍历的东西必须是列表或容器
    for(int i:v)
        cout<<i<<endl;

    // 迭代器：就是一个内存地址，用来找容器里面的元素的
    // 链式结构、树形结构、图形结构...等这些内存地址是不连续的，所以无法用简单的偏移方式推算
    // 那么就使用迭代器
    // 容器.begin()     头迭代器
    // 容器.begin()+Δi  次迭代器
    // 容器.end()       尾迭代器（空值）
    // 迭代器是指针变量的数组，里面全存内存地址

    // 有这么一个数组：
    //      0x01    0x78    0x32    0x11    （元素）
    //      0       1       2       3       （下标）
    // 通过下标偏移的方式来计算，实现“伪连续”

    // 这样写存储迭代器的变量：
    // vector<int>::iterator l = v.begin();
    vector<int>::iterator l = v.begin();
    // 解引用头迭代器试试：
    cout<<*l<<endl;
    // 解引用次迭代器：（加几就是第几代迭代器）
    cout<<*(l+1)<<endl;

    // 这个地方的插入指的是直接插入到提供的位置上
    v.insert(v.begin()+1,5);
    for(auto x:v)
        cout<<x<<endl;
    // 容器.clear()     清空
    v.clear();
    // 此时再输出容器长度的话，就为0
    cout<<v.size()<<endl;

// map
    m["哈哈"] = 50;
    cout<<m["哈哈"]<<endl;
    // 可以发现,是可以输出的,这就牛逼了
    // 如果调用一个键,且该键在容器内不存在,则自动创建该键
    // 何以见得?
    // 证明:
    map<string,int> test;           // 首先创建一个新 map 容器
    cout<<test.size()<<endl;        // 0
    cout<<test["不存在的键"]<<endl;  // 0
    cout<<test.size()<<endl;        // 1
    // 证毕 Q.E.D

    // 插入键:
    m.insert(make_pair("草",20));
    cout<<m["草"]<<endl;

    // 验证一个键是否存在:
    cout<<m.count("草")<<endl;          // 1
    cout<<m.count("不存在的键")<<endl;  // 0
    
    tempc::a = 10;
    tempc::b = 20;

    f(&tempc::a,&tempc::b);
    cout<<tempc::a<<" || "<<tempc::b<<endl;

    return 0;
}
