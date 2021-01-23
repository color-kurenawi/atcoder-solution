#include<iostream>
using namespace std;

int main(){
    int X, Y;
    cin >> X >> Y;

    if (X + 3 > Y && Y + 3 > X) {
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
    return 0;
}