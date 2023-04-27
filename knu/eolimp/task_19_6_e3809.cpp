// https://www.eolymp.com/uk/submissions/13606304
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

void solve() {
    int n;
    cin >> n;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > q1;
    priority_queue<pair<int, int>> q2;

    for (int i = 0; i < n; i++) {
        int a, b;
        
        cin >> a >> b;
        q1.push({a, b});
    }

    long long ans = 0;
    int h = 1;

    while (true) {
        if (q1.empty() && q2.empty()) {
            break;
        }

        if (q2.empty()) {
            h = q1.top().first;
        }

        if (!q1.empty()) {
            while (!q1.empty() && q1.top().first <= h) {
                q2.push({q1.top().second, q1.top().first});
                q1.pop();
            }
        }

        long long k = (h - q2.top().second);

        k *= q2.top().first;
        ans += k;
        q2.pop();
        h++;
    }

    cout << ans << "\n";
}

int main() {
    int i;
    cin >> i;
    while (i--) solve();
    
    return 0;
}