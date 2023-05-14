// https://www.eolymp.com/uk/submissions/13739190
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void dfs(const int node, vector<vector<int>>& ss, vector<int>& color, vector<int>& ans, bool& success) {
    color[node] = 1;

    for (auto chield : ss[node]) {
        if (color[chield] == 1)
            success = false;

        if (color[chield] == 0)
            dfs(chield, ss, color, ans, success);
    }

    color[node] = 2;
    ans.push_back(node);
}

void topologic_sort(vector<vector<int>>& ss, vector<int>& ans, bool& success) {
    auto n = ss.size();
    ans.clear();
    fill(ans.begin(), ans.end(), -1);
    success = true;

    vector<int> color(n, 0);

    for (int i = 0; i < n && success; i++)
        if (!color[i])
            dfs(i, ss, color, ans, success);

    reverse(ans.begin(), ans.end());
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> ss(n);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        --a, --b;
        ss[a].push_back(b);
    }

    vector<int> ans(n);
    bool success;

    topologic_sort(ss, ans, success);

    if (!success) {
        cout << -1 << endl;
        return 0;
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] + 1 << " ";
    }
        
    cout << endl;

    return 0;
}