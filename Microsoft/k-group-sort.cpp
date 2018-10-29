#include<bits/stdc++.h>
using namespace std;

int* kGroupSort(int *arr, int n, int k)
{
    map<int, vector<int> > ans;
    
    for(int i=0; i<n; i+=k)
    {
        vector<int> temp;
        string group = "";
        for(int j=0; j<k; j++)
        {
            temp.push_back(arr[i+j]);
            group += to_string(arr[i+j]);
        }

        ans.insert({stoi(group), temp});
    }

    int *ret = new int[n];
    int i=0;

    for(auto &group: ans)
        for(int num: group.second)
            ret[i++] = num;
    return ret;
}

int main()
{
    int arr[] = {1, 23, 4, 3, 8, 9};
    
    cout<<"Original array: ";
    for(int i=0;i<6;i++)
        cout<<arr[i]<<" ";
    cout<<endl;

    cout<<"2-Group Sort: ";
    int *ans = kGroupSort(arr, 6, 2);
    for(int i=0;i<6;i++)
        cout<<ans[i]<<" ";
    cout<<endl;

    cout<<"3-Group Sort: ";
    ans = kGroupSort(arr, 6, 3);
    for(int i=0;i<6;i++)
        cout<<ans[i]<<" ";
    cout<<endl;
    
}