// https://www.eolymp.com/uk/submissions/13606141
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

int main() {
    string s;
    priority_queue<pair<int, string>> q;
    map<string, int> mp;
    set<pair<int, string>> old;

    while (cin >> s) {
        string id;
        int cur;

        if (s == "ADD") {
            cin >> id >> cur;
            q.push({cur, id});
            mp[id] = cur;

        } else if (s == "CHANGE") {
            cin >> id >> cur;
            old.insert({mp[id], id});
            mp[id] = cur;
            q.push({cur, id});

        } else if (s == "POP") {
            while (true) {
                if(q.empty()) {
                    break;
                }

                auto curr = q.top();
                q.pop();

                if (old.count({curr.first, curr.second})) {
                    old.erase({curr.first, curr.second});

                } else {
                    cout << curr.second << " " << curr.first << "\n";
                    break;
                }
            }
        }

    }

    return 0;
}