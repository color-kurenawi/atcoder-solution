#include<iostream>
#include<vector>
using namespace std;

int main(){
    int N;
    vector<int> A;
    
    cin >> N;
    A.resize(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    int ans = 0;
    for (int i = 0; i < N; ++i) {
        int min_val = A[i];
        for (int j = i; j < N; ++j) {
            min_val = min(min_val, A[j]);
            int score = (j-i+1) * min_val;
            ans = max(ans, score);
        }
    }
    cout << ans << endl;
    return 0;
}