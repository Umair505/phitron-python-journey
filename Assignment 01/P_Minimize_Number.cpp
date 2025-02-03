#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int a[n];
    int sum = 0;
    bool flag = true;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        sum += a[i];
        if (a[i] % 2 != 0)
            flag = false;
    }
    int cnt = 0;
    if (flag)
    {
        bool flag1 = false;
        while (flag1 == false)
        {
            for (int i = 0; i < n; i++)
            {
                if (a[i] % 2 == 0)
                {
                    a[i] = a[i] / 2;
                }
                else
                {
                    flag1 = true;
                    break;
                }
            }
            cnt++;
        }
    }
    if(cnt==0)cout<<0;
    else
    cout << cnt-1;

    return 0;
}