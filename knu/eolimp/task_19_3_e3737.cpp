// https://www.eolymp.com/uk/submissions/13606003
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    bool success = true;

    cin >> n;
    vector<int> v(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }

    for (int i = 1; i <= n; i++) {
        if (2 * i <= n && v[i] > v[2 * i]) {
            success = false;
        }

        if (2 * i + 1 <= n && v[i] > v[2 * i + 1]) {
            success = false;
        }
    }

    cout << (success ? "YES" : "NO");
    return 0;
}