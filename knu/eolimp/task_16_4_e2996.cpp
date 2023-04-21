// https://www.eolymp.com/uk/submissions/13561161
#include <iostream>
#include <vector>

using namespace std;

int dfs(int node, int parr, vector<vector<int>> &ss, vector<int> &v) {
    int ans = v[node];
    int mn = 1e5;

    for (auto chield : ss[node]) {
        if (chield != parr) {
            mn = min(mn, dfs(chield, node, ss, v));
        }
    }
    
    ans += (mn == 1e5 ? 0 : mn);
    return ans;
}

void solve() {
    int n;
    cin >> n;

    vector<vector<int>> ss(n);
    vector<int> v(n);
    
    for (int i = 0; i < n; i++) {
        int k;
        cin >> v[i] >> k;

        for (int j = 0; j < k; j++) {
            int cur;
            cin >> cur;
            --cur;

            ss[i].push_back(cur);
            ss[cur].push_back(i);
        }
    }

    cout << dfs(0, -1, ss, v);
}

int main() {
    solve();
    return 0;
}