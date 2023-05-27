// https://www.eolymp.com/uk/submissions/13813175
#include <iostream>
#include <queue>
#include <stack>
#include <map>
using namespace std;

bool used[55][55] = {false};

int bfs(
    pair<int, int> start,
    pair<int, int> finish,
    const int & m,
    const int & n,
    const int & p,
    const int & q,
    map<pair<int, int>,
    pair<int, int>> &chield
){

    struct step { int x; int y; int d; };

    queue<step> que;
    que.push({start.first, start.second, 0});

    pair<int, int> run[8] = {{p, -q}, {p, q}, {-p, -q}, {-p, q}, {q, p}, {q, -p}, {-q, p}, {-q, -p}};
    int MAXARR = max(m, n) + 1;

    while (!que.empty()) {
        auto cur = que.front();
        que.pop();

        if (cur.x == finish.first && cur.y == finish.second) {
            return cur.d;
        }

        for (auto r : run) {
            if (
                cur.x + r.first <= m 
                && cur.x + r.first >= 1
                && cur.y + r.second <= n
                && cur.y + r.second >= 1
                && !used[cur.x + r.first][cur.y + r.second]
            ) {
                used[cur.x + r.first][cur.y + r.second] = true;
                que.push({cur.x + r.first, cur.y + r.second, cur.d + 1});
                chield[ {cur.x + r.first, cur.y + r.second}] = {cur.x, cur.y};
            }
        }
    }

    return -1;
}

void pq_horse(
    const int & m,
    const int & n,
    const int & p,
    const int & q,
    pair<int, int> & start,
    pair<int, int> &finish,
    int &ans,
    stack<pair<int, int>> &st
) {

    map<pair<int, int>, pair<int, int>> chield;
    ans = bfs(start, finish, m, n, p, q, chield);

    if (ans == -1) {
        while (!st.empty()) st.pop();
        return;
    }

    st.push(finish);
    pair<int, int> cur = finish;

    while (cur != start) {
        cur = chield[ {cur.first, cur.second}];
        st.push({cur.first, cur.second});
    }
}

int main() {
    int x1, y1, x2, y2;
    int n = 8, p = 2, q = 1;

    cin >> n;
    vector<vector<char>> v(n + 1, vector<char>(n + 1, '.'));
    bool setStart = false;
    
    for (int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            cin >> v[i][j];

            if (v[i][j] == '@' && !setStart) {
                setStart = true, x1 = i, y1 = j;
            
            } else if(v[i][j] == '@' && setStart) {
                x2 = i, y2 = j;
            
            } else if(v[i][j] == '#') {
                used[i][j] = true;
            }
        }
    }

    int ans;
    stack<pair<int, int>> st;
    pair<int, int> start = {x1, y1};
    pair<int, int> finish = {x2, y2};

    pq_horse(n, n, p, q, start, finish, ans, st);

    if (ans == -1) {
        cout << "Impossible" << endl;
        return 0;
    }

    while (!st.empty()) {
        auto cur = st.top();
        st.pop();
        v[cur.first][cur.second] = '@';
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << v[i][j];
        }

        cout << endl;
    }

    return 0;
}
