// https://www.eolymp.com/uk/submissions/13739212
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

void bfs_compSv(vector<vector<int>>& ss, const int countNode, vector<int>& compSv, int& countCompSv) {
    vector<bool> used(countNode, false);
    compSv.resize(countNode);
    fill(compSv.begin(), compSv.end(), 0);
    
    countCompSv = 0;

    for (int i = 0; i < countNode; i++) {
        if (!used[i]) {
            queue<int> q;
            q.push(i);
            used[i] = true;
            countCompSv++;

            while (!q.empty()) {
                auto cur = q.front();
                q.pop();
                compSv[cur] = countCompSv;

                for (auto chield : ss[cur]) {
                    if (!used[chield]) {
                        used[chield] = true;
                        q.push(chield);
                    }
                }
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> ss(n);

    for (auto i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        --a, --b;

        ss[a].push_back(b);
        ss[b].push_back(a);
    }

    vector<int> compSv;
    int countCompSv;

    bfs_compSv(ss, n, compSv, countCompSv);

    map<int, set<int>> mp;
    
    for(int i = 0; i < n; i++) {
        mp[compSv[i]].insert(i);
    }

    cout << countCompSv << "\n";

    for (auto d : mp) {
        cout << d.second.size() << "\n";
        
        for (auto k : d.second) {
            cout << k + 1 << " ";
        }
        
        cout << "\n";
    }

    return 0;
}