#include <bits/stdc++.h>
#include <windows.h>

using namespace std;

string comments[2048]={"致", "癌"
		, "晒妹SAGE" 
		, "我去，是初音未来", "这是芦苇"
		, "车万赛高"
		, "(`ヮ´ )σ`∀´) ﾟ∀ﾟ)σ ", "( ﾟ∀。) "
		, "(  ^w^)", "是吗？(　^ω^) ", "你看我语气很平和啊(　^ω^) ", "主观的错误的片面的扁平的(　^ω^) "
		, "哇你的好大诶(　^ω^) ", "sword new new(　^ω^) ", "(　^ω^)(`ε´ (つ*⊂) ", "吃了吗(　^ω^) ", "我不客气了\n(　^ω^)\n(つд⊂) "
		, "你要先吃饭，先洗澡，还是先吃我呢(　^ω^) "
		, "jmjp","jmjp(｀･ω･) ", "鸡密鸡排 ", "见面就跑 ", "鸡米键盘", "精美奖品 "
		, "纯度狂增，劲增，暴增百倍不止啊！ ", "还有这种好事？(´ﾟДﾟ`) ", "这个盘古生下来就力大无穷，有一天，他劈开了一个大鸡蛋 "
		, "吃点好的，不要吃屎 ", "在岛上看到太多椒麻鸡皮\n馋得不行\n转头去橙色软件一通搜索\n下单了两大包盐焗鸡皮\n坐等收货( ´ρ`)\n肥肥就是逊啦！ "};
string title, text;
int comments_number, conments_allnum,
	cookie_ID_capital, cookie_ID_lowercase,
	post_number;


int main(int argc, char const *argv[])
{
	// SetConsoleOutputCP(65001);
	cout<<"今天要PO些什么呢？\n\n";
	cin>>text;
	cout<<endl;
	srand(unsigned(time(0)));   //获取系统时间 
	for (int i=1;i<=15;i++)
	{
		cout<<"..." /*"无标题  "<<"无名氏  "<<"ID:"*/;
		for (int i=1;i<=3;i++)
		{
			cookie_ID_capital = 97+rand()%25;
			cookie_ID_lowercase = 65+rand()%25;
			post_number += rand();
			cout<<char (cookie_ID_capital)<<char (cookie_ID_lowercase);
		}
		comments_number = rand()%(i+rand()%25);//生成随机数 
		cout<<" || >>No."<<post_number<<endl<<"   "<<comments[comments_number]<<endl<<endl;
	}
	return 0;
}