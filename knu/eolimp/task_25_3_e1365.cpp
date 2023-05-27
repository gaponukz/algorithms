// https://www.eolymp.com/uk/submissions/13813319
#include <iostream>
#include <queue>
#include <stack>
#include <map>
#include <climits>
using namespace std;

void dejkstra(
    const vector<vector<pair<int, long long>>> &ss,
    const int &countNode,
    const int &start, vector<long long> &dist,
    vector<int> &parrent
) {

    dist.resize(countNode, LLONG_MAX);
    dist[start] = 0;

    parrent.resize(countNode, -1);
    parrent[0] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> q;
    q.push({0, start});

    while (!q.empty()) {
        int cur = q.top().second;
        long long curLen = q.top().first;
        q.pop();

        if (curLen < dist[cur]) {
            continue;
        } 

        for (auto chield : ss[cur]) {
            int to = chield.first;
            long long len = chield.second;

            if (dist[to] > dist[cur] + len) {
                dist[to] = dist[cur] + len;
                q.push({dist[to], to});
                parrent[to] = cur;
            }
        }
    }
}

int main() {
    int n, start, finish;

    cin >> n >> start >> finish;
    --start, --finish;

    vector<vector<pair<int, long long>>> ss(n);
    vector<long long> dist;
    vector<int> parrent;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            long long cur;
            cin >> cur;

            if (cur > 0 && i != j) {
                ss[i].push_back({j, cur});
            }
        }
    }

    dejkstra(ss, n, start, dist, parrent);
    printf("%d\n", dist[finish]);

    return 0;
}