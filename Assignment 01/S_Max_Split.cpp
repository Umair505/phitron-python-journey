#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int l=0,r=0,idx=0;
    string arr[1000];
    string ans ="";
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='L')l++;
        else r++;
        ans.push_back(s[i]);
        if(l==r)
        {
            arr[idx] = ans;
            ans = "";
            idx++;
            l=0;
            r=0;
        }
    } 
    cout<<idx<<endl;
    for(int i=0;i<idx;i++)
    {
        cout<<arr[i]<<endl;
    }
    return 0;
}