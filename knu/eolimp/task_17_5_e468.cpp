// https://www.eolymp.com/uk/submissions/13561272
#include <iostream>
using namespace std;

int MAX = 2147483647;
int MIN = -2147483648;

void solve() {
    int prev, cur;
    scanf("%d", &prev);
    
    while (scanf("%d", &cur) == 1) {
        if (cur < MIN || cur > MAX) {
            cout << "NO" << endl;
            return;
        }

        if (cur > prev) {
            MIN = prev;
        } else {
            MAX = prev;
        }

        prev = cur;
    }

    cout << "YES" << endl;
}

int main(){
    solve();
    return 0;
}