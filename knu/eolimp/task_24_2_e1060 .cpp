// https://www.eolymp.com/uk/submissions/13813063
#include <iostream>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
using namespace std;

vector<vector<int>> ss;

int main() {
    int n;
    cin >> n;
    
    char ms[(n + 2) * (n + 2)];
    int start, finish;
    
    bool used[(n + 2) * (n + 2)];
    memset(used, true, sizeof(used));

    for (int i = 1; i <= (n + 2) * (n + 2); i++) {
        char ch;
        bool kromka = i / (n + 2) == 0 || i / (n + 2) == n + 1 || i % (n + 2) == 1 || i % (n + 2) == 0;
        
        if (kromka) {
            ms[i] = 'O';
        
        } else {
            cin >> ch;
            ms[i] = ch;
            
            if (ch == '@') {
                start = i;
            } else if (ch == 'X') {
                finish = i;
            }

            if (ch != 'O') {
                used[i] = false;
            }
        }
    }

    queue<int> qu;
    stack<pair<int, int>> stack;

    used[start] = true;
    qu.push(start);

    int step[4] = {n + 2, -(n + 2), 1, -1};
    bool success = false;

    while (!qu.empty() && !success) {
        int node = qu.front();
        qu.pop();

        for (auto pr : step) {
            int cur = node + pr;

            if (cur <= (n + 2) * (n + 2) && cur > 0 && !used[cur]) {
                used[cur] = true;
                qu.push(cur);
                stack.push({node, cur});
                
                if (cur == finish) {
                    success = true;
                    break;
                }
            }
        }
    }

    if (!success) {
        cout << "N" << endl;
        return 0;
    }

    int cur = finish;
    ms[cur] = '+';

    while (!stack.empty()) {
        auto top = stack.top();
        stack.pop();

        if (top.second == cur && top.first != start) {
            ms[top.first] = '+';
            cur = top.first;
        }
    }

    cout << "Y" << endl;

    for (int i = n + 3; i <= (n + 2) * (n + 2) - (n + 2); i++) {
        bool kromka = i / (n + 2) == 0 || i / (n + 2) == n + 1 || i % (n + 2) == 1 || i % (n + 2) == 0;
        
        if (!kromka) {
            cout << ms[i];
        }

        if (i % (n + 2) == n + 1) {
            cout << endl;
        }
    }

    return 0;
}
