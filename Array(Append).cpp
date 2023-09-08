#include <iostream>

using namespace std;

int main()
{
    int numero[10], i, x;
    cout<<"Enter 10 array elements";
    for (i=0;i<9;i++)
        cin>>numero[i];
    cout << "\nInput an Element/Value: ";
    cin>>x;
    numero[i] = x;
    cout<<"The New Array is: ";
    for (i=0; i<10;i++)
        cout<<numero[i]<<" ";
    cout<<endl;
    return 0;
}
