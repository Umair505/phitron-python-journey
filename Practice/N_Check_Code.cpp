#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b;
    cin>>a>>b;
    string s;
    cin>>s;
    bool flag = false;
    for(int i=0;i<s.size();i++)
    {
        if( i!=a && !isdigit(s[i]))
        {
            flag = true;
            break;
        }
    }
    if(flag == true){
        cout<<"No";
        return 0;
    }
    if(s[a]=='-')
    {
        cout<<"Yes"<<endl;
        return 0;
    }
    if(s.size()!=a+b+1)cout<<"No"<<endl;
    else cout<<"No"<<endl;
    return 0;
}