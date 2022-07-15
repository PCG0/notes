# 方便补全
```cpp
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>


#include <time.h>
#include <bits/stdc++.h>



sqrt()
pow()

#include <windows.h>
system("pause");
SetConsoleOutputCP(65001); // 中文显示支持

ios::sync_with_stdio(false); 以关闭同步的方式加快cin的读入速度
```

# 摘抄

## 洛谷

### P5718 【深基4.例2】找最小值

```cpp
#include<bits/stdc++.h>//万能头文件
using namespace std;//using
int main()
{
    int n,a[10001];//定义
    cin>>n;//输入
    for(int i=1;i<=n;i++) cin>>a[i];//循环输入
    sort(a+1,a+n+1);//快速排序
    cout<<a[1];//输出最小答案
    return 0;//华丽结束
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;
int a[1100],n;
int main()
{
    cin >> n;
    for(int i = 0;i < n;i++) cin >> a[i];
    cout << *min_element(a,a+n);
    // 函数名：min_element
    // 函数原型：min_element(_ForwardIterator __first, _ForwardIterator __last)
    // 函数作用：返回一个数组里的最小值的迭代器（因为是迭代器所以求值时要加上 *）
    return 0;
}
```



### P5705 【深基2.例7】数字反转

```cpp
#include <cstdio>
using namespace std;

char a, b, c, d;
int main()
{
    // scanf/printf 相比 cin/cout\tt cin/coutcin/cout 快得多，应对多数题目绰绰有余。
    scanf("%c%c%c.%c", &a, &b, &c, &d);
    printf("%c.%c%c%C", d, c, b, a);
    return 0;
}
```

还有另外一种解法，也值得摘抄：

```cpp
#include<bits/stdc++.h>
using namespace std;

string a;
int main()
{
    cin >> a;
    reverse(a.begin(), a.end());
    cout << a;
    return 0;
}
```



### P5710 【【深基3.例2】数的性质】

```cpp
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int x;
bool a, b;
int main(){
    scanf("%d", &x);
    a = !(x & 1), b = (x > 4 && x <= 12);//a满足性质1，b满足性质2
    printf("%d %d %d %d", a & b, a | b, (a && !b || b && !a), !a && !b);
   //按条件输出就好啦QWQ
}
```


### P1421 小玉买文具

```cpp
#include <iostream>
using namespace std;

int a, b, A;
double B;
int main()
{ 
  cin >> a >> b;
  A = a * 10 + b;
  B = A / 19;
  cout << B << endl; 
  return 0;
}
```
嘿嘿，这题对新手十分友好，我也能独立做出来。


### P1046 [NOIP2005 普及组] 陶陶摘苹果

**题目描述**

陶陶家的院子里有一棵苹果树，每到秋天树上就会结出 101010 个苹果。苹果成熟的时候，陶陶就会跑去摘苹果。陶陶有个 303030 厘米高的板凳，当她不能直接用手摘到苹果的时候，就会踩到板凳上再试试。

现在已知 101010 个苹果到地面的高度，以及陶陶把手伸直的时候能够达到的最大高度，请帮陶陶算一下她能够摘到的苹果的数目。假设她碰到苹果，苹果就会掉下来。

**正解**

```cpp
#include <iostream>
using namespace std;

int height[20],H,s;
int main()
{
    for(int i=0; i<3;i++) cin >> height[i];
    cin >> H;
    H += 30;
    for(int i=0; i<3;i++) s+=!(H<height[i]);
    cout << s;
}
```
ps：抄的。


### P1001 A+B Problem

**题目描述**

输入两个整数 a,ba, ba,b，输出它们的和（∣a∣,∣b∣≤109|a|,|b| \le {10}^9∣a∣,∣b∣≤109）。

**正解**

```cpp
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int a,b;
    cin >> a >> b;
    cout << a+b << endl;
    return 0;
}
```
ps：抄的。

## 编程猫社区

### 孤言-C++教程第5弹-代码练习3

Q1
```cpp
#include <iostream>
using namespace std;

int main()
{
    int lv;
    cin >> lv;
    if (lv > 15)
        cout << "%%%%tql" << endl;
    else
        cout << 16 - lv << endl;
    return 0;
}
```
其实跟A+B问题差不多，只不过多了个if的应用。
