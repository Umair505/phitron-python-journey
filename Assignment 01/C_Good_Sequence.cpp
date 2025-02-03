#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    int f[n];
    map<int,int>mp;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        mp[a[i]]++;
    } 
    int sum = 0;
    for(auto i:mp)
    {
        if(i.second>=i.first)
        {
            sum += (i.second - i.first);
        }
        else
        {
            sum+=i.second;
        }
    }
    cout<<sum<<endl;
    return 0;
}