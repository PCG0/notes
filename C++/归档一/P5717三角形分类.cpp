// #include <bits/stdc++.h>
// using namespace std;

// int main(int argc, char const *argv[])
// {
// 	int l[3]; bool Rt, At, Ot, It, Et, tr;
// 	for(int i=1;i<=3;i++) cin>>l[i];
// 	sort(l+1, l+3+1);
// 	// for(int i=1;i<=3;i++) cout<<l[i];
// 	tr=l[1]+l[2]>l[3]&&l[1]+l[3]>l[2]&&l[2]+l[3]>l[1]&&l[1]-l[2]<l[3]&&l[1]-l[3]<l[2]&&l[3]-l[2]<l[1];
// 	Rt=pow(l[1], 2)+pow(l[2], 2) == pow(l[3], 2);
// 	At=pow(l[1], 2)+pow(l[2], 2) >= pow(l[3], 2);
// 	Ot=pow(l[1], 2)+pow(l[2], 2) <= pow(l[3], 2);
// 	It=pow(l[1], 2) == pow(l[2], 2)||pow(l[2], 2) == pow(l[3], 2)||pow(l[1], 2) ==pow(l[3], 2);
// 	Et=pow(l[1], 2) == pow(l[2], 2)&&pow(l[2], 2) == pow(l[3], 2);
// 	if(Rt&&tr) cout<<"Right triangle"<<endl;
// 	else if(At&&tr) cout<<"Acute trianglee"<<endl;
// 	else if(Ot&&tr) cout<<"Obtuse triangle"<<endl;
// 	if(It) cout<<"Isosceles triangle"<<endl;
// 	else if(Et) cout<<"Equilateral triangle"<<endl;
// 	else if(!Rt&&!At&&!Ot&&!It&&!Et) cout<<"Not triangle"<<endl;
// 	return 0;
// }