// https://www.eolymp.com/uk/submissions/13813357
#include <iostream>
#include <queue>
#include <stack>
#include <map>
#include <climits>
using namespace std;

void dejkstra(
    const vector<vector<pair<int, long long>>>& ss,
    const int& countNode,
    const int& start, vector<long long>& dist,
    vector<int>& parrent
){

    dist.resize(countNode);
    fill(dist.begin(), dist.end(), LLONG_MAX);
    dist[start] = 0;

    parrent.resize(countNode);
    fill(parrent.begin(), parrent.end(), -1);
    parrent[start] = -1;

    priority_queue< pair<long long, int> > q;
    q.push({ 0, start });

    while (!q.empty()) {
        auto u = q.top();
        q.pop();

        int curNode = u.second;
        long long curLen = u.first;
        if (curLen > dist[curNode])
            continue;

        for (auto chield : ss[curNode]) {
            int to = chield.first, len = chield.second;
            
            if (dist[to] > dist[curNode] + len) {
                dist[to] = dist[curNode] + len;
                q.push({ dist[to], to });
                parrent[to] = curNode;
            }
        }
    }
}

int main() {
    int n, m, start, finish;
    cin >> n >> m >> start >> finish;
    --start, --finish;

    vector<vector<pair<int, long long>>> ss(n);
    
    for (int i = 0; i < m; i++) {
        int a, b;
        long long c;

        cin >> a >> b >> c;
        --a, --b;
        ss[a].push_back({ b, c });
        ss[b].push_back({ a, c });
    }

    vector<long long> dist;
    vector<int> parrent;
    
    dejkstra(ss, n, start, dist, parrent);
    
    cout << dist[finish] << endl;

    stack<int> st;
    int cur = finish;
    st.push(cur + 1);
    
    while (cur != start) {
        cur = parrent[cur];
        st.push(cur + 1);
    };

    while (!st.empty()) {
        cout << st.top() << " ";
        st.pop();
    }
    
    return 0;
}